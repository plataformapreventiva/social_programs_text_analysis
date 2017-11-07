#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(tidyverse)

ui <- shinyUI(fluidPage(
  titlePanel("Programas Sociales Similares"),
  sidebarLayout(
    mainPanel(
      plotOutput("plot1", width = "90%", click = "plot_click"),
      tags$head(tags$style(
        '#plot1 {
				cursor: pointer;
				}'))
      #div(tableOutput("table"), style = "font-size:120%")
    ),
    sidebarPanel(
      div(tableOutput("table"), style = "font-size:120%")
    )
  )
))

server <- shinyServer(function(input, output, session) {
  sims <- read_csv('../data/similarities_df_triangular.csv') %>% select(-cve_programa)
  
  clean_name <- function(x){
    ifelse(nchar(x)<50, x, paste(substring(x,1,50),'...'))
  }
  
  colnames(sims) <- c(sims$nombre_programa, 'nombre_programa')
  
  sims.g <- sims %>% gather(nombre_programa2, similar, -nombre_programa) %>% 
    mutate(similar = as.numeric(similar),
           nombre_programa_clean=clean_name(nombre_programa),
           nombre_programa_clean2=clean_name(nombre_programa2)) 
  
  programas <- unique(sims.g %>% select(nombre_programa_clean))
  sims.g$nombre_programa_clean <- ordered(sims.g$nombre_programa_clean, levels=rev(programas$nombre_programa_clean))
  sims.g$nombre_programa_clean2 <- ordered(sims.g$nombre_programa_clean2, levels=programas$nombre_programa_clean)
  
  sims.g <- sims.g  %>%
    filter(!is.na(similar))
  
  makeReactiveBinding('sims.g')
  
  output$plot1 <- renderPlot({
    # Corrplot
    ggplot(sims.g, aes(x = nombre_programa_clean, y = nombre_programa_clean2)) +
      geom_point(aes(size = similar, colour=similar)) + 
      scale_colour_distiller(palette = "RdYlBu", direction=1,
                             values= c(-0.4, 0.2, 0.4, 0.6, 0.8, 1)) +
      scale_size_area(max_size=5) +
      theme_light(base_size = 20) +
      labs(x = "", y = "") +
      theme(axis.ticks = element_blank(),
            axis.text.x = element_text(size = 9,
                                       angle = 330, hjust = 0),
            axis.text.y = element_text(size = 9)
      ) + 
      theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
            panel.background = element_blank(),
            legend.position="none")
  }, height = 800, width = 1000 ) 
  
  etable <- eventReactive(input$plot_click, {
    

    # Get 1 datapoint within 15 pixels of click, see ?nearPoints
    np <- nearPoints(sims.g, input$plot_click,
                     xvar = 'nombre_programa_clean',
                     yvar = 'nombre_programa_clean2',
                     maxpoints=1 , threshold = 3)
    res <- t(np[c('nombre_programa', 'nombre_programa2', 'similar')])
    rownames(res) <- c('Programa Social', 'Programa Social', 'Similitud')
    colnames(res) <- c('')
    return(res)
  })
  
  output$table <- renderTable({
    etable()
  }, include.colnames=FALSE)
})


# Run the application 
shinyApp(ui = ui, server = server)

