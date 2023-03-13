import customtkinter

import calculos

TITLE = "Calculadora - Custom Tkinter"
WIDTH = 470
HEIGHT = 620

# Define a localização para português brasileiro


class Calculadora(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # CONFIGS WINDOW
        self.title(TITLE)
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.main_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        ######################

        # Entrada das OPERAÇÕES
        self.label_operacao_value = customtkinter.StringVar()
        self.label_operacao = customtkinter.CTkLabel(self.main_frame,
                                                     text="0 + 1",
                                                     textvariable=self.label_operacao_value,
                                                     anchor="e")
        self.label_operacao.grid(row=0, sticky='nsew', padx=(10, 10))
        ####################

        # ENTRADA do USUARIO que mostrará resultado
        self.entrada_value = customtkinter.StringVar()
        self.limpa_valor_entrada()
        self.entrada = customtkinter.CTkEntry(self.main_frame,
                                              justify="right",
                                              textvariable=self.entrada_value,
                                              fg_color="transparent",
                                              font=("CTkFont", 50),
                                              border_width=0,
                                              height=40, corner_radius=0)
        # remove o cursor de texto que pisca
        self.entrada.configure(insertontime=0)
        self.entrada.grid(row=1, sticky="nsew", pady=(10, 50))
        self.entrada.bind("<Key>", self.k_formata_text)
        #################

        # BOTÕES
        self.botoes_frame = customtkinter.CTkFrame(
            self.main_frame, corner_radius=0, fg_color="transparent")
        self.botoes_frame.grid(row=2, sticky="nsew")
        self.botoes_frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.botoes_frame.rowconfigure(0, weight=1)

        # ROW 0
        self.button_mod, self.render_button_mod = self.button(
            "%", (0, 0), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("%"))
        self.button_CE, self.render_button_CE = self.button(
            "CE", (1, 0), "#323232", "#3c3c3c", command=self.limpa_valor_entrada)
        self.button_C, self.render_button_C = self.button(
            "C", (2, 0), "#323232", "#3c3c3c", command=self.limpa_tudo)
        self.button_clear, self.render_button_clear = self.button(
            "<x", (3, 0),  "#323232", "#3c3c3c", command=lambda: self.remove_ultimo_caracter())

        # ############# ROW 1
        self.button_1_div_x, self.render_button_1_div_x = self.button(
            "1/x", (0, 1), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("1/"))
        self.button_square, self.render_button_square = self.button(
            "x²", (1, 1), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("pow"))
        self.button_root_square, self.render_button_root_square = self.button(
            "√x", (2, 1), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("sqrt"))
        self.button_div, self.render_button_div = self.button(
            "/", (3, 1),  "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("/"))

        # ############# ROW 2
        self.button7, self.render_button7 = self.button(
            "7", (0, 2), command=lambda: self.insere_valor_entrada("7"))
        self.button8, self.render_button8 = self.button(
            "8", (1, 2), command=lambda: self.insere_valor_entrada("8"))
        self.button9, self.render_button9 = self.button(
            "9", (2, 2), command=lambda: self.insere_valor_entrada("9"))
        self.button_x, self.render_button_x = self.button(
            "X", (3, 2),  "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("X"))

        # ############ Row 3
        self.button4, self.render_button4 = self.button(
            "4", (0, 3), command=lambda: self.insere_valor_entrada("4"))
        self.button5, self.render_button5 = self.button(
            "5", (1, 3), command=lambda: self.insere_valor_entrada("5"))
        self.button6, self.render_button6 = self.button(
            "6", (2, 3), command=lambda: self.insere_valor_entrada("6"))
        self.button_minus, self.render_button_minus = self.button(
            "-", (3, 3), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("-"))

        # ############ Row 4
        self.button1, self.render_button1 = self.button(
            "1", (0, 4), command=lambda: self.insere_valor_entrada("1"))
        self.button2, self.render_button2 = self.button(
            "2", (1, 4), command=lambda: self.insere_valor_entrada("2"))
        self.button3, self.render_button3 = self.button(
            "3", (2, 4), command=lambda: self.insere_valor_entrada("3"))
        self.button_plus, self.render_button_pus = self.button(
            "+", (3, 4), "#323232", "#3c3c3c", command=lambda: self.seleciona_operacao("+"))

        # ############ Row 5
        self.button_plus_minus, self.render_button_plus_minus = self.button(
            "+/-", (0, 5), command=lambda: self.seleciona_operacao("negative"))
        self.button0, self.render_button0 = self.button(
            "0", (1, 5), command=lambda: self.insere_valor_entrada("0"))
        self.button_float, self.render_button_float = self.button(
            ",", (2, 5), command=lambda: self.insere_valor_entrada(","))
        self.button_result, self.render_button_result = self.button(
            "=", (3, 5), "#80c6fe", "#6da9d8", "#323232", command=self.calcula)
        
    # WIDGET BOTÕES
    def button(self, text: str, pos: tuple,
               fg_color="#3c3c3c",
               hover_color="#323232", text_color="white", 
               command=lambda: print("botao")):
        
        botao = customtkinter.CTkButton(self.botoes_frame,
                                        corner_radius=5,
                                        font=("CTkFont", 19),
                                        fg_color=fg_color,
                                        hover_color=hover_color,
                                        text_color=text_color,
                                        height=70,
                                        text=text,
                                        command=command
                                        )
        render_botao = botao.grid(column=pos[0], row=pos[1], padx=(2, 2),
                                  pady=(2, 2))
        return botao, render_botao

    # FUNÇÕES DA ENTRADA
    def insere_valor_entrada(self, text):
        texto_atual = self.entrada_value.get()
        if text == ',' in texto_atual:
            return

        self.entrada.insert('end', text)
        self.formata_texto()

    def formata_texto(self):
        valor_atual = self.entrada_value.get()
        if len(valor_atual) < 1:
            self.limpa_valor_entrada()
        else:
            valor_formatado = self.adiciona_mascara_digitando(valor_atual)
            self.entrada_value.set(valor_formatado)

    # formata apenas numeros inteiros
    def adiciona_mascara_digitando(self, texto):
        texto_sem_ponto = self.elimina_pontuacao(texto)
        if texto_sem_ponto.isnumeric():
            texto = f"{int(texto_sem_ponto):,}".replace(",", ".")
        return texto

    def limpa_tudo(self):
        self.limpa_valor_entrada()
        self.label_operacao_value.set("")

    def limpa_valor_entrada(self):
        self.entrada_value.set('0')

    def remove_ultimo_caracter(self):
        tamanho_entrada = len(self.entrada_value.get())
        if tamanho_entrada > 1:
            self.entrada.delete(tamanho_entrada - 1, 'end')
        else:
            self.limpa_valor_entrada()

    def k_formata_text(self, event):
        current_value = self.entrada_value.get()
        # Se caracter for uma virgula e não existir na entrada
        se_for_virgula = event.char == ',' and current_value.count(',') < 1
        # se for digito ou uma virgula
        if event.char.isdigit() or se_for_virgula:
            # Adicionar o novo valor à última posição da entrada
            self.insere_valor_entrada(event.char)
        elif event.keysym == "BackSpace":
            self.remove_ultimo_caracter()
        # Impedir que outros caracteres que não sejam números sejam inseridos
        return 'break'

    def seleciona_operacao(self, operacao):
        value = self.entrada_value.get()
        if operacao in ["sqrt", "pow", '1/', 'negative']:
            value = f"{operacao}({value})"
        else:
            value = f"{value} {operacao}"

        self.label_operacao_value.set(value)

    # transforma texto de Ex.: 1.000,01 para 1000.01
    def elimina_pontuacao(self, texto) -> str:
        return texto.replace('.', '').replace(",", ".")

    # transforma valor: int or float de Ex.: 1000.01 para 1.000,01
    def adiciona_pontuacao(self, texto) -> str:
        def padrao(x): return f"{x:,}".replace(
            ".", "<").replace(",", ".").replace("<", ",")
        return padrao(texto)

    # transforma a string operação Ex.:"1250.35 + 0.5" para "1.250,35 + 0,5"
    def adiciona_ponto_operacao(self, operacao):
        operacao_lista = operacao.split(' ')
        for i, valor in enumerate(operacao_lista):
            if valor.isdigit() or valor.replace('.', '').isdigit() or valor.isnumeric():
                operacao_lista[i] = self.adiciona_pontuacao(eval(valor))

        operacao_str = ' '.join(operacao_lista)

        return self.substitui_operadores(operacao_str, 'valor')

    def operadores(self):
        # tipo: dicionario
        # chave = simbolo
        # valor = operacao ou função
        return {
            "+": "+",
            "X": "*",
            "-": "-",
            "/": "/",
            "%": "%",
            "sqrt": "calculos.sqrt",
            "pow": "calculos.pow_square",
            "1/": "calculos.one_divided_n",
            "negative": "calculos.negative"
        }

    def substitui_operadores(self, operacao, modo='chave'):
        operadores = self.operadores()
        for i, j in operadores.items():
            if modo == 'chave':
                operacao = operacao.replace(i, j)
            else:
                operacao = operacao.replace(j, i)

        return operacao

    def calcula_adiciona_ponto(self, operacao):
        try:
            resultado = eval(operacao)
            return self.adiciona_pontuacao(resultado)
        except ZeroDivisionError:
            return 'ZeroDivisionError'

    def calcula_resultado(self, operacao_value, entrada_value):
        operadores = self.operadores()
        def existe_op(x): return any([i in x for i in operadores.values()])

        operacao = self.substitui_operadores(operacao_value)  # '4 + 1'
        operacao_lista = operacao.split(' ')  # ['4', '+', '1']

        existe_operador = existe_op(operacao)
        if existe_operador:
            if len(operacao_lista) > 2:
                operacao_lista[0] = entrada_value
            else:
                operacao_lista.append(entrada_value)
                if len(operacao_lista) == 2:
                    operacao_lista.pop()

            operacao = ' '.join(operacao_lista)
            resultado = operacao
        else:
            operacao = resultado = entrada_value

        print(operacao_lista)
        return self.calcula_adiciona_ponto(resultado), self.adiciona_ponto_operacao(operacao)

    def calcula(self):
        # pega o valor do label_operacao
        label_operacao_value = self.label_operacao_value.get()
        entrada_value = self.entrada_value.get()  # pega o valor do entrada_value

        operacao_value = self.elimina_pontuacao(label_operacao_value)
        entrada_value = self.elimina_pontuacao(entrada_value)

        resultado, operacao = self.calcula_resultado(
            operacao_value, entrada_value)

        self.label_operacao_value.set(operacao)
        self.entrada_value.set(resultado)


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop()
