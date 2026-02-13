import flet as ft

def main(page: ft.Page):
    mensagem= ft.Text("Escolha o nome certo!")
    resposta_correta = "Henry Danger"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabens"
        else:
            mensagem.value = "Resposta errada"
        page.update()

    page.title = "Game: Adivinhe a Imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "blue"

    page.add(
       ft.Column(
           controls=[
               ft.Text(
                   "Qual o nome do ajudante do capitao MEN",
                   size=24,
                   weight="bold"
               ),
               ft.Image(
                   src="image/henry.jpg",
                   height=200
               ),
               ft.Row(
                   controls=[
                       ft.Button(
                           content="Henry Danger",
                           on_click=verificar_resposta
                       ),
                       ft.Button(
                           content="Jasper",
                           on_click=verificar_resposta
                       ),
                       ft.Button(
                           content="Schwoz",
                           on_click=verificar_resposta
                       ),
                   ],
                   alignment=ft.MainAxisAlignment.CENTER
               ),
               mensagem
           ],
           horizontal_alignment=ft.CrossAxisAlignment.CENTER   
       )
    )

ft.run(main)