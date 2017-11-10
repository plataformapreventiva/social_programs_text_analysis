import re
import pandas as pd
import boto3


def notempty(string):
    """
    Checks if string exists
    if it does no exists returns an empty string

    :params: string to check
    :rtype: str
    """
    if string:
        return string
    else:
        return ''


def obj_esp_union(row):
    """
    Function that concatenates all general and specific objetives
    of each subprogram

    :param: row of a dataframe

    :returns: text_union
    :rtype: string
    """
    text_union = ("""{subprograma} {obj_g1} {obj_e1} {obj_e2} {obj_e3} {obj_e4} {obj_e5} {pob_obj} 
                    """.format(subprograma=notempty(row['nombre_subprograma']),
                               obj_g1=notempty(row['obj_gral_prog_1']),
                               obj_e1=notempty(row['obj_esp_prog_1']),
                               obj_e2=notempty(row['obj_esp_prog_2']),
                               obj_e3=notempty(row['obj_esp_prog_3']),
                               obj_e4=notempty(row['obj_esp_prog_4']),
                               obj_e5=notempty(row['obj_esp_prog_5']),
                               pob_obj=notempty(row['pob_obj_prog'])
                              ))
    return text_union


def all_objetivos_union(rows):
    """
    Concatenates all rows of subprogramas to have
    only one text for the programa

    :param: rows of dataframe
    :rtype: string
    """
    nombres = [x for x in rows['nombre_programa']]
    nombres = " ".join(list(set(nombres)))
    objetivos_grales = [x for x in rows['obj_gral_prog_1']]
    objetivos_grales = " ".join(list(set(objetivos_grales)))

    return nombres + ' ' + objetivos_grales + ' ' + " ".join(rows['objetivos_especificos'])


def read_file():
    """
    Reads cuaps file from s3 and join objectives for each program

    Returns:
    -------
    df_p: dataframe that contains each progrm as row and
          a column of description that has all the text of the objectives
    """
    s3_file = 'https://s3-us-west-2.amazonaws.com/sedesol-open-data/cuaps_sedesol.csv'
    programas = pd.read_csv(s3_file)
    # Drop progrms without objective
    programas = programas.dropna(subset=['obj_gral_prog_1'], axis=0)
    programas['cve_padron'] = programas['cve_padron'].apply(lambda x: str(x).zfill(4))
    # Concatenate specific objectives
    programas['objetivos_especificos'] = programas.apply(lambda x: obj_esp_union(x), axis=1)

    # Join specific subprograms
    df_p1 = programas.groupby(['cve_programa'])['objetivos_especificos'].apply(lambda x: " ".join(set(x)))
    # Join program names
    df_p2 = programas.groupby(['cve_programa'])['nombre_programa'].apply(lambda x: " ".join(set(x)))
    # Join general objectives
    df_p3 = programas.groupby(['cve_programa'])['obj_gral_prog_1'].apply(lambda x: " ".join(set(x)))

    # Union all
    df_p = pd.concat([df_p1, df_p2, df_p3], axis=1)
    df_p = df_p.reset_index()
    # Leave only one column
    df_p['descripcion'] = df_p['nombre_programa'] + ' ' + df_p['obj_gral_prog_1'] + ' ' + df_p['objetivos_especificos']
    df_p.set_index('cve_programa', inplace=True)
    return df_p
