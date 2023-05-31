import customtkinter as ctk
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from pathlib import Path
from PIL import Image,ImageTk

janela = Tk()

OUTPUT_PATH = Path(__file__).parent

class Application():

    class BackEnd():

        def conecta_db():
            con = mysql.connector.connect(host='localhost', database='users', user='root', password='mysqlimt')
            
            if con.is_connected():
                db_info = con.get_server_info()
                print("conectado ao servidor",db_info)
                cursor = con.cursor()
                cursor.execute("select database();")
                linha = cursor.fetchone()
                print("conectado ao banco de dados", linha)
            if con.is_connected():
                cursor.close()
                con.close()
                print("conexão ao mySQL foi encerrada")
            
            pass
        
    def  __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaLogin()
        janela.mainloop()
        self.cadastrarUsuario()
        self.conf()
    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    #config janela
    def tela(self):
        janela.geometry("1280x720")
        janela.resizable(False,False)
        janela.configure(bg = "#272727")
    
    def cadastrarUsuario(self,nome,RA,senha):
            con = mysql.connector.connect(host='localhost', database='users', user='root', password='mysqlimt')
            
            if con.is_connected():
                db_info = con.get_server_info()
                print("conectado ao servidor",db_info)
                cursor = con.cursor()
                cursor.execute("select database();")
                linha = cursor.fetchone()
                print("conectado ao banco de dados", linha)
           
            self.RACadastro = RA
            self.senhaCadastro= senha
            self.nomeCadastro  = nome 
            cursor = con.cursor()
            comandoCadastrar = f"INSERT INTO usuarios (nome,RA,password) VALUES('{nome}','{RA}','{senha}')"
            cursor.execute(comandoCadastrar)
            con.commit()

    def conf(self,RA,senha):
        def quiz():
            frameMenu.pack_forget()

            canvas = Canvas(
                janela,
                bg = "#383838",
                height = 720,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            var = ctk.BooleanVar()
            global respostaInt 
            respostaInt = 0
            global score
            score = 0

            perguntas = [
                ["Quais destes tipos de dados são mutáveis em Python? Selecione todas as alternativas \ncorretas:", "a) Strings", "b) Listas", "c) Tuplas", "d) Dicionário", 24, 2],
                ["Qual caractere que, quando usando em uma string, é conhecido como caractere de \nescape?", "\\", "","",0,4],
                ["Qual é a extensão de arquivo usada para scripts Python?","a) .py","b) .pt","c) .pyt","d) .px", 1,1],
                ["O Python é uma linguagem de programação orientada a objetos?", "a) Verdadeiro", "b) Falso", "", "", 1, 3],
                ["Qual dos seguintes métodos é usado para obter o comprimento de uma lista em Python?","a) length()","b) size()","c) count()","d) len()",4,1],
                ["O Python é uma linguagem compilada?","a) Verdadeiro","b) Falso", "", "", 0, 3],
                ["O que é um dicionário em Python?","a) Uma estrutura de dados que armazena pares de chave-valor.","b) Um tipo de variável que armazena valores numéricos.","c) Uma função embutida para ordenar listas.","d) Um tipo de loop utilizado para repetir um bloco de código.",1,1],
                ["Qual é o operador usado para concatenar duas strings em Python?","a) +","b) *","c) /","d) -",1,1],
                ["Qual é a instrução utilizada para interromper um loop em Python?","break","","","",0,4], 
                ["Quais desses métodos podem ser usados para remover um elemento de uma lista?", "a) remove()", "b) delete()", "c) pop()", "d) clear()", 134, 2]
                # Puxar essas perguntas do bd
            ]

            def setrespostaInt(num):
                global respostaInt
                respostaInt = num
            
            def clicabotao(n,r):
                global score
                btn1.deselect()
                btn2.deselect()
                btn3.deselect()
                btn4.deselect()
                if n == r:
                    score += 1
                    print(score)

            def respondeVF(n,r):
                global score
                dic= {"Verdadeiro": 1, "Falso": 0}
                if r == "Verdadeiro" or r == "Falso":
                    if n == dic[r]:
                        score += 1
                        print(score)

            def responde(n,r):
                global score
                if n.lower() == r.lower().rstrip("\n"):
                    score += 1
                else:
                    pass

            def desliga(b1, b2, b3):
                b1.deselect()
                b2.deselect()
                b3.deselect()

            def respostaM():
                resp = ""
                for i in blist:
                    if i.get() == i._onvalue:
                        resp += str(i._onvalue)
                if resp != "":
                    return int(resp)

            def impedeEnter():
                return "break"

            def tiraWidget(wid):
                wid.place_forget()

            btn1 = ctk.CTkCheckBox(janela, text="")
            btn2 = ctk.CTkCheckBox(janela, text="", onvalue=2)
            btn3 = ctk.CTkCheckBox(janela, text="", onvalue=3)
            btn4 = ctk.CTkCheckBox(janela, text="", onvalue=4)

            blist = [btn1, btn2, btn3, btn4]

            alt1 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white")
            alt2 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white")
            alt3 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white")
            alt4 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white")

            altlist = [alt1,alt2,alt3,alt4]

            vOuF = ctk.CTkComboBox(janela, values=["Verdadeiro", "Falso"], state="readonly")

            respostaTB = ctk.CTkTextbox(janela, width=1000, height=20, activate_scrollbars=False, font=("Consolas", 20))
            respostaTB.bind("<Return>", impedeEnter())

            botaoResponde_image = PhotoImage(
                file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_responde.png")))
            botaoResponde = Button(
                image=botaoResponde_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#272727",
                activebackground='#272727',
                command=lambda: print("button_1 clicked"),
                relief="flat"
            )
            botaoResponde.place(
                x=939.0,
                y=586.0,
                width=283.0,
                height=82.0
            )
            botaoRespondetxt = ctk.CTkLabel(janela,text="Próxima Questão", font=("Consolas", 30), text_color="#FFE873", bg_color="#306998")
            botaoRespondetxt.place(x=960.0,y=608.0)

            pergunta= ctk.CTkLabel(janela,font=("Consolas", 25), text_color="white")
            pergunta.place(relx = 0.05, y = 40)

            resposta = ctk.CTkLabel(janela, text="Resposta:",font=("Consolas", 26),text_color="white")

            for x in perguntas:
                pergunta.configure(text=x[0])
                
                for i in altlist:
                    tiraWidget(i)
                for i in blist:
                    tiraWidget(i)
                tiraWidget(vOuF)
                tiraWidget(respostaTB)
                tiraWidget(resposta)
                
                respostaInt = 0

                if x[-1] == 1 or x[-1] == 2:
                    for i in range(1,5):
                        match i:
                            case 1:
                                alt1.configure(text=x[i], text_color="white")
                                alt1.place(relx=0.07, rely=0.2)
                                btn1.place(relx=0.9,rely=0.2)
                            case 2:
                                alt2.configure(text=x[i], text_color="white")
                                alt2.place(relx=0.07, rely=0.35)
                                btn2.place(relx=0.9,rely=.35)
                            case 3:
                                alt3.configure(text=x[i], text_color="white")
                                alt3.place(relx=0.07, rely=0.50)
                                btn3.place(relx=0.9,rely=0.5)
                            case 4:
                                alt4.configure(text=x[i], text_color="white")
                                alt4.place(relx=0.07, rely=0.65)
                                btn4.place(relx=0.9,rely=0.65)

                    if x[-1] == 1:
                        btn1.configure(command=lambda: [setrespostaInt(1),desliga(btn2, btn3, btn4)])
                        btn2.configure(command=lambda: [setrespostaInt(2),desliga(btn1, btn3, btn4)]) 
                        btn3.configure(command=lambda: [setrespostaInt(3),desliga(btn2, btn1, btn4)])
                        btn4.configure(command=lambda: [setrespostaInt(4),desliga(btn2, btn3, btn1)])
                        botaoResponde.configure(command=lambda : [var.set(1), clicabotao(x[-2],respostaInt)])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                    
                    if x[-1] == 2:
                        btn1.configure(command=lambda: [setrespostaInt(1)])
                        btn2.configure(command=lambda: [setrespostaInt(2)]) 
                        btn3.configure(command=lambda: [setrespostaInt(3)])
                        btn4.configure(command=lambda: [setrespostaInt(4)])
                        botaoResponde.configure(command=lambda : [var.set(1), setrespostaInt(respostaM()),clicabotao(x[-2],respostaInt)])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))

                if x[-1] == 3 or x[-1] == 4:
                    resposta.place(relx = 0.05, rely = 0.2) 
                    if x[-1] == 3:
                        vOuF.place(relx = 0.05, rely = 0.3)
                        botaoResponde.configure(command=lambda : [var.set(1), respondeVF(x[-2], vOuF.get())])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                    if x[-1] == 4:
                        respostaTB.delete("1.0", ctk.END)
                        respostaTB.place(relx = 0.05, rely = 0.3)
                        botaoResponde.configure(command=lambda : [var.set(1), responde(x[1], respostaTB.get("1.0", ctk.END))])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))      

                janela.update()
                btn1.wait_variable(var)

            def mostraScore(botaoResponde, botaoRespondetxt):
                for i in altlist:
                    tiraWidget(i)
                for i in blist:
                    tiraWidget(i)
                tiraWidget(vOuF)
                tiraWidget(respostaTB)
                tiraWidget(resposta)
                tiraWidget(pergunta)
                botaoResponde.destroy()
                botaoRespondetxt.destroy()

                botaoResponde = Button(
                image=botaoResponde_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#272727",
                activebackground='#272727',
                command=lambda: var.set(1),
                relief="flat"
                )
                botaoResponde.place(
                    x=939.0,
                    y=586.0,
                    width=283.0,
                    height=82.0
                )
                botaoRespondetxt = ctk.CTkLabel(janela,text="Finalizar", font=("Consolas", 36), text_color="#FFE873", bg_color="#306998")
                botaoRespondetxt.place(x=985.0,y=606.0)
                botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                global score
                mostrascore = ctk.CTkLabel(janela,font=("Consolas", 64),text_color="white", text="A sua pontuação é: {}".format(score))
                mostrascore.place(relx=0.22,rely=0.35)
                btn1.wait_variable(var)
                mostrascore.destroy()
                botaoResponde.destroy()
                botaoRespondetxt.destroy()
                menu()
            
            mostraScore(botaoResponde, botaoRespondetxt)

            janela.resizable(False, False)
            janela.mainloop()

        def menu():
            frameLogin.pack_forget()
            frameLogin2.pack_forget()

            global frameMenu
            frameMenu = ctk.CTkFrame(master=janela,width=1280,height=720)
            frameMenu.pack()

            canvas = Canvas(
                frameMenu,
                bg = "#272727",
                height = 720,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            canvas.create_rectangle(
                306.0,
                0.0,
                1280.0,
                720.0,
                fill="#383838",
                outline="")

            botaoiniciar_image = PhotoImage(
            file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_5.png")))

            botaoiniciar = Button(
                master= canvas,
                image=botaoiniciar_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: quiz(),
                relief="flat"
            )
            botaoiniciar.place(
                x=1005,
                y=626,
                width=250.0,
                height=70.0
            )
            
            botaoiniciartxt = ctk.CTkLabel(frameMenu,text="Iniciar", font=("Consolas", 40), text_color="#FFE873", bg_color="#306998")
            botaoiniciartxt.place(x=1050,y=636)

            botaoiniciartxt.bind("<Button-1>", botaoiniciar.cget("command"))

            botaoquiz_image = PhotoImage(
            file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_4.png")))
            botaoquiz = Button(
                master= frameMenu,
                image=botaoquiz_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: print("button_4 clicked"),
                relief="flat"
            )
            botaoquiz.place(
                x=0.0,
                y=128.0,
                width=306.0,
                height=107.0
            )

            botaoquiztxt = ctk.CTkLabel(frameMenu,text="Quiz", font=("Consolas", 40), text_color="#306998", bg_color="#363636")
            botaoquiztxt.place(x=20.0,y=155.0)

            botaoResultados_image = PhotoImage(
                file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_un.png")))
            botaoResultados = Button(
                master= frameMenu,
                image=botaoResultados_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: print("button_3 clicked"),
                relief="flat"
            )
            botaoResultados.place(
                x=0.0,
                y=250.0,
                width=306.0,
                height=107.0
            )

            botaoResultadostxt = ctk.CTkLabel(frameMenu,text="Resultados", font=("Consolas", 40), text_color="#FFE873", bg_color="#2F2F2F")
            botaoResultadostxt.place(x=20.0,y=278.0)

            buttonquestoes = Button(
                master= frameMenu,
                image=botaoResultados_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: print("button_2 clicked"),
                relief="flat"
            )
            buttonquestoes.place(
                x=0.0,
                y=374.0,
                width=306.0,
                height=107.0
            )

            buttonquestoestxt = ctk.CTkLabel(frameMenu,text="Questões", font=("Consolas", 40), text_color="#FFE873", bg_color="#2F2F2F")
            buttonquestoestxt.place(x=20.0,y=400.0)

            sair_image = PhotoImage(
                file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_1.png")))
            sair = Button(
                master= frameMenu,
                image=sair_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#272727",
                activebackground='#272727',
                command=lambda: print("button_1 clicked"),
                relief="flat"
            )
            sair.place(
                x=250.0,
                y=675.0,
                width=46.0,
                height=46.0
            )

            profileImage = PhotoImage(
                file=(r"{}\assets\{}".format(OUTPUT_PATH,"image_1.png")))
            profileI = canvas.create_image(
                28.0,
                697.0,
                image=profileImage
            )

            ra = ctk.CTkLabel(frameMenu,text=RA, font=("Consolas", 30), text_color="white", bg_color="#272727")
            ra.place(x=60.0, y=680)

            canvas.create_text(
                367.0,
                139.0,
                anchor="nw",
                text="Tutorial:\n\n● O Quiz apresentará as questões em ordem aleatória.\n\n● Seu tempo será cronometrado, mas não será salvo no sistema.\n\n● As questões podem variar de alternativa, resposta múltipla, \n\nverdadeiro ou falso e resposta curta.\n\n● Após inserir a sua resposta, clique em próxima questão.\n\n● Quando tiver respondido todas as questões, clique em\n\n “Finalizar Quiz”.",
                fill="#FFFFFF",
                font=("Consolas", 25 * -1)
            )

            quizTxt = ctk.CTkLabel(frameMenu,text="Quiz", font=("Consolas", 64), text_color="white", fg_color="#383838")
            quizTxt.place(x=710.0, y=39.0)

            printQuiz = ctk.CTkLabel(frameMenu,text="print(“Quiz”)", font=("Consolas", 36 * -1), text_color="white")
            printQuiz.place(x=28.0, y=40.0)

            botaoLista = [botaoiniciar, botaoquiz, botaoResultados,buttonquestoes]
            textoLista = [botaoiniciartxt, botaoquiztxt, botaoResultadostxt, buttonquestoestxt]
            conta = 0

            for i in textoLista:
                i.bind("<Button-1>", botaoLista[conta].cget("command"))
                #ativar clique botao
                conta += 1

            janela.resizable(False, False)
            janela.mainloop()
            
        con = mysql.connector.connect(host='localhost', database='users', user='root', password='mysqlimt')
        cont = 0
        if con.is_connected():
                db_info = con.get_server_info()
                print("conectado ao servidor",db_info)
                cursor = con.cursor()
                cursor.execute("select database();")
                linha = cursor.fetchone()
                print("conectado ao banco de dados", linha)

                self.usuarioEntry = RA
                self.senhaEntry= senha

                cursor = con.cursor() 
                consulta = (F"select RA FROM  usuarios;")  
                cursor.execute(consulta)
                
                puxa = list(cursor.fetchall())

                consultaSenha = (f"select password FROM usuarios;") 
                cursor.execute(consultaSenha)

                puxaSenha = list(cursor.fetchall())
                
                print(puxa)
                for ra in puxa:
                   
                    if str(ra) == "('{}',)".format(self.usuarioEntry):
                         for senha in puxaSenha:
                            if str(senha) == "('{}',)".format(self.senhaEntry):
                                menu()
                            else:
                                print('erro')        
                    else:
                        print('erro')
        else:   
            pass

    def telaLogin(self):
        
        #frame de login
        global frameLogin 
        frameLogin = ctk.CTkFrame(master=janela,width=500,height=720)
        frameLogin.pack(side=RIGHT)

        global frameLogin2
        frameLogin2 = ctk.CTkFrame(master=janela,width=1280,height=720, fg_color = "#272727")
        frameLogin2.pack(side=RIGHT)
        
        img= ImageTk.PhotoImage(Image.open(r"{}\assets\{}".format(OUTPUT_PATH,"pngwing.com_resized_1.png")))
        labelImage = ctk.CTkLabel(master=frameLogin2, image=img, text="")
        labelImage.place(relx=0.3,rely=0.3)
        printtxt = ctk.CTkLabel(master=frameLogin2, text="print(", text_color="#FFE873", font=("Consolas", 64))
        printtxt.place(relx=0.22,rely=0.1)
        quiztxt = ctk.CTkLabel(master=frameLogin2, text="\"Quiz\"", text_color="#306998", font=("Consolas", 64))
        quiztxt.place(relx=0.49,rely=0.1)
        partxt = ctk.CTkLabel(master=frameLogin2, text=")", text_color="#FFE873", font=("Consolas", 64))
        partxt.place(relx=0.76,rely=0.1)
        # widgets dentro da tela de login
        self.titulo=  ctk.CTkLabel(master=frameLogin, text='Faça o Login', font = ('Roboto', 20, 'bold'), text_color= ('white') )
        self.titulo.place(x=190, y=100)
        #widgets usuario
        usuarioEntry= ctk.CTkEntry(master=frameLogin, placeholder_text="RA do usuario",width=300,font=('Roboto', 14, 'bold'))
        usuarioEntry.place(x=100, y=200)
        self.usuarioLabel=ctk.CTkLabel(master=frameLogin, text="O campo do RA do usuario é obrigatorio", text_color="green",font=("Roboto",10)).place(x=100, y=230)
        
        senhaEntry= ctk.CTkEntry(master=frameLogin, placeholder_text="Senha do usuario",width=300,font=('Roboto', 14, 'bold'), show = "*")
        senhaEntry.place(x=100, y=265)
        self.senhaLabel=ctk.CTkLabel(master=frameLogin, text="O campo de senha do usuario é obrigatorio", text_color="green",font=("Roboto",10)).place(x=100, y=295)

        self.loginButton = ctk.CTkButton(master=frameLogin, text="LOGIN",width=300,command=lambda: self.conf(usuarioEntry.get(),senhaEntry.get()))
        self.loginButton.place(x=100,y=345)

        self.register_span = ctk.CTkLabel(master=frameLogin, text="Se não tem cadastro").place(x=100, y=385)
        
        def telaCadastro():

            #removendo o frame de login
            frameLogin.pack_forget()
            frameLogin2.pack_forget()

            #frame de cadastro
            frameCadastro = ctk.CTkFrame(master=janela,width=500,height=720)
            frameCadastro.pack(side=RIGHT)
            
            frameLogin2.pack(side=RIGHT)

            labelImage.place(relx=0.3,rely=0.3)

            titulo=  ctk.CTkLabel(master=frameCadastro, text='Faça seu cadastro', font = ('Roboto', 20, 'bold'), text_color= ('white') )
            titulo.place(x=155, y=100)

            RAEntry= ctk.CTkEntry(master=frameCadastro, placeholder_text="insira o RA do usuario",width=300,font=('Roboto', 14, 'bold'))
            RAEntry.place(x=100, y=200)

            senhaEntry= ctk.CTkEntry(master=frameCadastro, placeholder_text="insira a Senha do usuario",width=300,font=('Roboto', 14, 'bold'), show = "*")
            senhaEntry.place(x=100, y=250)
    
            NomeEntry= ctk.CTkEntry(master=frameCadastro, placeholder_text="insira o Nome do usuario",width=300,font=('Roboto', 14, 'bold'))
            NomeEntry.place(x=100, y=300)
            
            def back():

                frameCadastro.pack_forget()

                frameLogin.pack(side=RIGHT)
                frameLogin2.pack_forget()
                frameLogin2.pack(side=RIGHT)
                
                pass
            save_Button = ctk.CTkButton(master=frameCadastro, text="REGISTRAR",width=145, fg_color="green",hover_color="#014B05",command=lambda:  self.cadastrarUsuario(NomeEntry.get(),RAEntry.get(),senhaEntry.get()))
            save_Button.place(x=275,y=385)

            voltarButton = ctk.CTkButton(master=frameCadastro, text="Voltar",width=145,command=back, fg_color="gray", hover_color="#202020")
            voltarButton.place(x=85, y=385)
            pass

        registerButton = ctk.CTkButton(master=frameLogin, text="REGISTER", width=150,fg_color="green", hover_color="#2d9334",command= telaCadastro)
        registerButton.place(x=250,y=385)

        return frameLogin
        
Application()

janela.mainloop()