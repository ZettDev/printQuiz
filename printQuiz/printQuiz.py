import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from pathlib import Path
from PIL import Image,ImageTk
import time
import numpy as np
import random

janela = Tk()

OUTPUT_PATH = Path(__file__).parent

global botao_image 
botao_image = PhotoImage(
file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_5.png")))
global botaoLixoimg
botaoLixoimg = PhotoImage(
file=(r"{}\assets\{}".format(OUTPUT_PATH,"lixo.png")))

class Application():
    global score
    score = 0
    global scoreMax
    scoreMax = 10

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


            if self != "" and nome != "" and senha != "":
                try:
                    self.RACadastro = RA
                    self.senhaCadastro= senha
                    self.nomeCadastro  = nome 
                    cursor = con.cursor()
                    comandoCadastrar = f"INSERT INTO usuarios (nome,RA,password) VALUES('{nome}','{RA}','{senha}')"
                    cursor.execute(comandoCadastrar)
                    con.commit()
                    messagebox.showinfo(title="registro",message="Seu cadastro foi registrado com suscesso")
                except mysql.connector.IntegrityError as e:
                    print("Erro de integridade:", e)
                    messagebox.showinfo(title="registro",message="RA já utilizado.")
                except mysql.connector.Error as e:
                    print("Erro ao conectar ao banco de dados:", e)
                    messagebox.showinfo(title="registro",message="Erro ao conectar ao banco de dados, tente novamente mais tarde.")
            else:
                messagebox.showinfo(title="registro",message="Informações faltantes.")

    def conf(self,RA,senha):
        def quiz():
            frameMenu.pack_forget()

            var = ctk.BooleanVar()
            global respostaInt 
            respostaInt = 5
            global score
            score = 0

            cursor.execute("select * from questoes")

            perguntas = []

            for i in cursor.fetchall():
                perguntas.append(i)

            global scoreMax
            scoreMax = len(perguntas)

            random.shuffle(perguntas)

            def setrespostaInt(num):
                global respostaInt
                respostaInt = num
            
            def respondeAlt(n):
                global score
                for i in blist:
                    i.deselect()
                if n == respostaInt:
                    score += 1

            def respondeVF(n):
                global score
                desliga(btn1, btn2)
                if n == respostaInt:
                    score += 1

            def responde(n,r):
                global score
                if n.lower() == r.lower().rstrip("\n"):
                    score += 1
                else:
                    pass

            def desliga(*botoes):
                for i in botoes:
                    i.deselect()

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

            alt1 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white", wraplength=1190)
            alt2 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white", wraplength=1190)
            alt3 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white", wraplength=1190)
            alt4 = ctk.CTkLabel(janela,font=("Consolas", 25),text_color="white", wraplength=1190)

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

            pergunta= ctk.CTkLabel(janela,font=("Consolas", 25), text_color="white", wraplength=1216)
            pergunta.place(relx = 0.05, y = 40)

            resposta = ctk.CTkLabel(janela, text="Resposta:",font=("Consolas", 26),text_color="white")

            contaPerguntas = ctk.CTkLabel(janela,font=("Consolas", 30),text_color="white")
            contaPerguntas.place(x=830.0,y=608.0)
            contador = 0

            for x in perguntas:
                pergunta.configure(text=x[0])

                contador += 1
                contaPerguntas.configure(text= "{}/{}".format(contador,len(perguntas)))
                
                for i in altlist:
                    tiraWidget(i)
                for i in blist:
                    tiraWidget(i)
                tiraWidget(vOuF)
                tiraWidget(respostaTB)
                tiraWidget(resposta)
                
                respostaInt = 5

                if x[-1] == 1 or x[-1] == 2:
                    for i in range(1,5):
                        match i:
                            case 1:
                                alt1.configure(text=x[i])
                                alt1.place(relx=0.07, rely=0.2)
                                btn1.place(relx=0.9,rely=0.2)
                            case 2:
                                alt2.configure(text=x[i])
                                alt2.place(relx=0.07, rely=0.35)
                                btn2.place(relx=0.9,rely=.35)
                            case 3:
                                alt3.configure(text=x[i])
                                alt3.place(relx=0.07, rely=0.50)
                                btn3.place(relx=0.9,rely=0.5)
                            case 4:
                                alt4.configure(text=x[i])
                                alt4.place(relx=0.07, rely=0.65)
                                btn4.place(relx=0.9,rely=0.65)

                    if x[-1] == 1:
                        btn1.configure(command=lambda: [setrespostaInt(1),desliga(btn2, btn3, btn4)])
                        btn2.configure(command=lambda: [setrespostaInt(2),desliga(btn1, btn3, btn4)]) 
                        btn3.configure(command=lambda: [setrespostaInt(3),desliga(btn2, btn1, btn4)])
                        btn4.configure(command=lambda: [setrespostaInt(4),desliga(btn2, btn3, btn1)])
                        botaoResponde.configure(command=lambda : [var.set(1), respondeAlt(x[-2])])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                    
                    if x[-1] == 2:
                        btn1.configure(command=lambda: [setrespostaInt(1)])
                        btn2.configure(command=lambda: [setrespostaInt(2)]) 
                        btn3.configure(command=lambda: [setrespostaInt(3)])
                        btn4.configure(command=lambda: [setrespostaInt(4)])
                        botaoResponde.configure(command=lambda : [var.set(1), setrespostaInt(respostaM()),respondeAlt(x[-2])])
                        botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                    
                if x[-1] == 3:
                    alt1.configure(text="Verdadeiro")
                    alt1.place(relx=0.07, rely=0.2)
                    btn1.place(relx=0.9,rely=0.2)
                    alt2.configure(text="Falso")
                    alt2.place(relx=0.07, rely=0.35)
                    btn2.place(relx=0.9,rely=.35)
                    btn1.configure(command=lambda: [setrespostaInt(1),desliga(btn2)])
                    btn2.configure(command=lambda: [setrespostaInt(0),desliga(btn1)]) 
                    botaoResponde.configure(command=lambda : [var.set(1), respondeVF(x[-2])])
                    botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))
                if x[-1] == 4:
                    resposta.place(relx = 0.05, rely = 0.2) 
                    respostaTB.delete("1.0", ctk.END)
                    respostaTB.place(relx = 0.05, rely = 0.3)
                    botaoResponde.configure(command=lambda : [var.set(1), responde(x[1], respostaTB.get("1.0", ctk.END))])
                    botaoRespondetxt.bind("<Button-1>", botaoResponde.cget("command"))      

                janela.update()
                btn1.wait_variable(var)

            def mostraScore(botaoResponde, botaoRespondetxt):
                widgetLista = [vOuF, respostaTB, resposta, pergunta]

                for i, j, k in zip(altlist, blist, widgetLista):
                    tiraWidget(i)
                    tiraWidget(j)
                    tiraWidget(k)

                tiraWidget(contaPerguntas)
                
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
                mostrascore = Label(janela,anchor="center",justify="center",font=("Consolas", 28),foreground="white",background="#272727", text="A sua pontuação é: {} de {} perguntas".format(score, len(perguntas)))
                mostrascore.place(relx=0.22,rely=0.35)
                btn1.wait_variable(var)
                mostrascore.destroy()
                botaoResponde.destroy()
                botaoRespondetxt.destroy()

                cursor.execute(f"select id from usuarios where RA = \"{raAdap}\"")
                idAluno = int(str(cursor.fetchone()).strip("(,)"))
                
                cursor.execute(f"select max(tentativa) from tentativas where idAluno = {idAluno}")

                tentativa = str(cursor.fetchone()).strip("(,)")
                if tentativa == "None":
                    tentativa = 1
                else:
                    tentativa = int(tentativa) + 1

                print(tentativa)

                cursor.execute(f"insert into tentativas values({idAluno},{tentativa},{score},{scoreMax})")
                con.commit()
                menu()
            
            mostraScore(botaoResponde, botaoRespondetxt)

            janela.resizable(False, False)
            janela.mainloop()

        def telaResultados():
            frameMenu.pack_forget()

            global frameResultados
            frameResultados = ctk.CTkFrame(master=janela,width=1280,height=720)
            frameResultados.pack()

            canvas = Canvas(
                frameResultados,
                bg = "#272727",
                height = 720,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            canvas.place(x=0,y=0)

            def voltaMenu():
                frameResultados.destroy()
                menu()

            botaoVoltar = Button(
                master=frameResultados,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#272727",
                activebackground='#272727',
                command=lambda : voltaMenu(),
                relief="flat"
            )
            botaoVoltar.place(
                x=28.0,
                y=15.0,
                width=283.0,
                height=82.0
            )

            botaoVoltarText = ctk.CTkLabel(frameResultados,text="Voltar", font=("Consolas", 40), text_color="#FFE873", bg_color="#306998")
            botaoVoltarText.place(x=100.0,y=32.0)
            botaoVoltarText.bind("<Button-1>", botaoVoltar.cget("command"))

            style = ttk.Style()
    
            style.theme_use("default")

            style.configure("Treeview",
                font = ("Consolas", 20),
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)

            style.configure("Treeview.Heading",
                font = ("Consolas", 20),
                background="#565b5e",
                foreground="white",
                relief="flat")
            
            style.map("Treeview.Heading", background=[('active', '#565b5e')])

            tree = ttk.Treeview(canvas, selectmode="none", height= 10)

            tree["columns"] = ("Nome", "Tentativa", "Nota")

            tree.column("#0", width=0, stretch=NO) 
            tree.column("Nome", width=200, stretch=True)
            tree.column("Tentativa", width=160, stretch=True)
            tree.column("Nota", width=100, stretch=True)

            tree.heading("#0", text="", anchor=W)
            tree.heading("Nome", text="Nome")
            tree.heading("Tentativa", text="Tentativa")
            tree.heading("Nota", text="Nota")

            

            scrollbar = ctk.CTkScrollbar(canvas, orientation="vertical", command=tree.yview, height=100)
            tree.configure(yscrollcommand=scrollbar.set)

            def disable_column_click(event):
                col = tree.identify_column(event.x)
                if col:
                    return "break"

            tree.bind("<Button-1>", disable_column_click)

            tree.place(relx = 0.32, rely = 0.3)
            scrollbar.place(x= 870, rely = 0.3)

            if admin == 1:
                def mudouPergunta(*args):
                    tree.delete(*tree.get_children())
                    for i,j,k in zip(listaAlunos, idAlunos, nomeAlunos):
                        if alunos.get() == i:
                            cursor.execute(f"select * from tentativas where idAluno = {j}")
                            tentativas = cursor.fetchall()
                            for x in tentativas:
                                tree.insert("", END, text="1", values=(f"{k}", f"{x[1]}", f"{x[2]}\\{x[3]}"))

                opcao = ctk.StringVar()
                alunos = ctk.CTkComboBox(frameResultados,width=270,font=("Consolas", 20), dropdown_font=("Consolas", 20), state="readonly", variable=opcao)
                alunos.place(x=75, y= 150)
                
                resultadostxt = ctk.CTkLabel(frameResultados,font=("Consolas", 40),text_color="white", text="Resultados:", bg_color="#272727")
                resultadostxt.place(x=530, y=30)

                cursor.execute(f"select * from usuarios")

                puxaAlunos = list(cursor.fetchall())

                listaAlunos = []
                idAlunos = []
                nomeAlunos = []
                for i in puxaAlunos:
                    listaAlunos.append(i[2])
                    idAlunos.append(i[0])
                    nomeAlunos.append(i[1])

                alunos.configure(values = listaAlunos)

                opcao.trace("w",mudouPergunta)
            else:
                seusResultadostxt = ctk.CTkLabel(frameResultados,font=("Consolas", 40),text_color="white", text="Seus Resultados:", bg_color="#272727")
                seusResultadostxt.place(x=465, y=30)

                cursor.execute(f"select id, nome from usuarios where RA = \"{raAdap}\"")
                idNome = cursor.fetchone()
                print(idNome[0])
                
                cursor.execute(f"select * from tentativas where idAluno = {idNome[0]}")
                tentativas = cursor.fetchall()
                for x in tentativas:
                    tree.insert("", END, text="1", values=(f"{idNome[1]}", f"{x[1]}", f"{x[2]}\\{x[3]}"))


        def telaQuestoes(criar):
            frameMenu.pack_forget()

            global frameQuestoes
            frameQuestoes = ctk.CTkFrame(master=janela,width=1280,height=720)
            frameQuestoes.pack()

            canvas = Canvas(
                frameQuestoes,
                bg = "#272727",
                height = 720,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            canvas.place(x=0,y=0)

            def impedeEnter():
                return "break"

            def perguntaAlternativa():
                opcao1.place(relx=0.03, rely=0.345)
                opcao2.place(relx=0.03, rely=0.495)
                opcao3.place(relx=0.03, rely=0.645)
                opcao4.place(relx=0.03, rely=0.795)

                alt1.place(relx=0.03, rely=0.30)
                btn1.place(relx=0.9,rely=0.37)

                alt2.place(relx=0.03, rely=0.45)
                btn2.place(relx=0.9,rely=0.52)

                alt3.place(relx=0.03, rely=0.60)
                btn3.place(relx=0.9,rely=0.67)

                alt4.place(relx=0.03, rely=0.75)
                btn4.place(relx=0.9,rely=0.82)

            def perguntaVerdadeiro():
                verdadeiro.place(relx=0.03, rely=0.345)
                btn1.place(relx=0.9,rely=0.37)

                falso.place(relx=0.03, rely=0.495)
                btn2.place(relx=0.9,rely=0.52)

            def perguntaR():
                respostaTxt.place(relx=0.03, rely=0.30)
                resposta.place(relx=0.03, rely=0.345)

            def desligaBotoes(*botoes):
                for i in botoes:
                    i.deselect()

            def limpaText(*caixaTexto):
                for i in caixaTexto:
                    i.delete("1.0", ctk.END)

            def retiraWidget():
                for i, j, k in zip(blist, altlist, opcaoLista):
                    i.place_forget()
                    j.place_forget()
                    k.place_forget()

                verdadeiro.place_forget()
                falso.place_forget()

                respostaTxt.place_forget()
                resposta.place_forget()

            def check(indice):
                if admin == 1:
                    cadastrar(indice)
                else:
                    popup = Toplevel()
                    popup.title("Digite a senha")
                    popup.geometry("300x150")
                    popup.grab_set()

                    def checaSenha():
                        if senhaEntry.get() == "admin":
                            if cadastrar(indice) == 0:
                                messagebox.showinfo("Erro", "Falta de informações sobre a questão.")
                            else:
                                messagebox.showinfo("Sucesso", "Senha correta!")
                            popup.destroy()
                        else:
                            messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")
                            senhaEntry.delete(0, END)
    
                    senhaTxt = Label(popup, text="Senha:")
                    senhaEntry = Entry(popup, show="*")
                    botaoEnviar = Button(popup, text="Enviar", command=lambda: checaSenha())
                    
                    senhaTxt.pack()
                    senhaEntry.pack()
                    botaoEnviar.pack()
            
            def cadastrar(indice):
                if indice in [1,2]:
                    return cadastrarAlt(indice, False)
                elif indice == 3:
                    return cadastrarVerdadeiro(False)
                else:
                    return cadastrarRes(False)

            def cadastrarAlt(tipo, substituir):
                sql = "insert into questoes values("
                sqlLista = []
                altsLista = []
                alts = ""

                perg = str(pergunta.get("1.0", ctk.END).strip("\n"))
                sqlLista.append(f"\"{perg}\"") #pega pergunta

                for i, j in zip(blist, opcaoLista):
                    if i.get() != 0:
                        altsLista.append(i.get()) #pega n alt correta
                    alt = str(j.get("1.0", ctk.END)).strip("\n") #pega alternativas
                    sqlLista.append(f"\"{alt}\"")

                for i in altsLista:
                    alts += str(i)

                if alts == "":
                    messagebox.showwarning(title="Aviso",message="Alternativa correta não selecionada.")
                    return 0
                
                sqlLista.append(int(alts))
                sqlLista.append(tipo)

                for i in sqlLista:
                    if not isinstance(i, str):
                        break
                    if i == "":
                        messagebox.showwarning(title="Aviso",message="Erro, uma ou mais alternativas vazias.")
                        return 0
                    sql += i+","

                sql+=f"{sqlLista[5]},{tipo})"

                if substituir:
                    cursor.execute(f"delete from questoes where pergunta = \"{perguntaAtual}\"")
                    cursor.execute(sql)
                    con.commit()
                    editarInter()
                else:
                    cursor.execute(sql)
                    con.commit()

                desligaBotoes(btn1, btn2, btn3, btn4)
                limpaText(opcao1, opcao2, opcao3, opcao4, pergunta)

            def cadastrarVerdadeiro(substituir):
                sql = "insert into questoes values("

                perg = str(pergunta.get("1.0", ctk.END).strip("\n"))

                if perg == "":
                    messagebox.showwarning(title="Aviso",message="Erro, pergunta vazia.")
                    return 0

                sql += f"\"{perg}\",null,null,null,null,"

                if btn1.get() == 1:
                    sql += "1,3)"
                elif btn2.get() == 2:
                    sql += "0,3)"
                else:
                    messagebox.showwarning(title="Aviso",message="Erro, você deve selecionar Verdadeiro ou Falso.")
                    return 0

                if substituir:
                    cursor.execute(f"delete from questoes where pergunta = \"{perguntaAtual}\"")
                    cursor.execute(sql)
                    con.commit()
                    editarInter()
                else:
                    cursor.execute(sql)
                    con.commit()

                desligaBotoes(btn1, btn2)
                limpaText(pergunta)

            def cadastrarRes(substituir):
                sql = "insert into questoes values("

                perg = str(pergunta.get("1.0", ctk.END).strip("\n"))
                if perg == "":
                    messagebox.showwarning(title="Aviso",message="Erro, pergunta vazia.")
                    return 0
                sql += f"\"{perg}\","

                resp = str(resposta.get("1.0", ctk.END).strip("\n"))
                if resp == "":
                    messagebox.showwarning(title="Aviso",message="Erro, pergunta vazia.")
                    return 0
                sql += f"\"{resp}\",null,null,null,null,4)"

                if substituir:
                    cursor.execute(f"delete from questoes where pergunta = \"{perguntaAtual}\"")
                    cursor.execute(sql)
                    con.commit()
                    editarInter()
                else:
                    cursor.execute(sql)
                    con.commit()
                
                limpaText(pergunta, resposta)

            def deletarQuestao(botaoLixo):
                cursor.execute(f"delete from questoes where pergunta = \"{perguntaAtual}\"")
                con.commit()
                botaoLixo.configure(state="disabled")
                desligaBotoes(btn1, btn2, btn3, btn4)
                limpaText(opcao1, opcao2, opcao3, opcao4, pergunta, resposta)
                editarInter()

            def voltaMenu():
                frameQuestoes.destroy()
                menu()
            
            btn1 = ctk.CTkCheckBox(canvas, text="")
            btn2 = ctk.CTkCheckBox(canvas, text="", onvalue=2)
            btn3 = ctk.CTkCheckBox(canvas, text="", onvalue=3)
            btn4 = ctk.CTkCheckBox(canvas, text="", onvalue=4)

            blist = [btn1, btn2, btn3, btn4]

            perguntaTxt = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Pegunta:")

            alt1 = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Alternativa 1:")
            alt2 = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Alternativa 2:")
            alt3 = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Alternativa 3:")
            alt4 = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Alternativa 4:")

            altlist = [alt1,alt2,alt3,alt4]

            opcao1 = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))
            opcao2 = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))
            opcao3 = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))
            opcao4 = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))

            opcaoLista = [opcao1, opcao2, opcao3, opcao4]

            for i in opcaoLista:
                i.bind("<Return>", impedeEnter())

            verdadeiro = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Verdadeiro:")
            falso = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Falso:")

            respostaTxt = ctk.CTkLabel(canvas,font=("Consolas", 25),text_color="white", text="Resposta:")

            resposta = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))
            resposta.bind("<Return>", impedeEnter())
            
            pergunta = ctk.CTkTextbox(frameQuestoes, width=1000, height=65, activate_scrollbars=False, font=("Consolas", 20))
            pergunta.bind("<Return>", impedeEnter())

            botaoVoltar = Button(
                master=frameQuestoes,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#272727",
                activebackground='#272727',
                command=lambda : voltaMenu(),
                relief="flat"
            )
            botaoVoltar.place(
                x=28.0,
                y=15.0,
                width=283.0,
                height=82.0
            )

            botaoVoltarText = ctk.CTkLabel(frameQuestoes,text="Voltar", font=("Consolas", 40), text_color="#FFE873", bg_color="#306998")
            botaoVoltarText.place(x=100.0,y=32.0)
            botaoVoltarText.bind("<Button-1>", botaoVoltar.cget("command"))

            pergunta.place(relx=0.03, rely=0.195)
            perguntaTxt.place(relx=0.03, rely=0.15)

            def editarInter():
                cursor.execute("select * from questoes")

                perguntas = []

                for i in cursor.fetchall():
                    perguntas.append(i)

                def mudouPergunta(*args):
                    botaoLixo.configure(state="normal")

                    retiraWidget()
                    desligaBotoes(btn1, btn2, btn3, btn4)
                    limpaText(pergunta, opcao1, opcao2, opcao3, opcao4, resposta)

                    for i in perguntas:
                        if i[0] == perguntasBox.get():
                            global perguntaAtual
                            perguntaAtual = i[0]
                            pergunta.insert(ctk.END, i[0])
                            match(i[-1]):
                                case 1:
                                    perguntaAlternativa()
                                    opcao1.insert(ctk.END, i[1])
                                    opcao2.insert(ctk.END, i[2])
                                    opcao3.insert(ctk.END, i[3])
                                    opcao4.insert(ctk.END, i[4])

                                    for x in blist:
                                        if i[5] == x._onvalue:
                                            x.select()
                                    btn1.configure(command=lambda: desligaBotoes(btn2, btn3, btn4))
                                    btn2.configure(command=lambda: desligaBotoes(btn1, btn3, btn4)) 
                                    btn3.configure(command=lambda: desligaBotoes(btn2, btn1, btn4))
                                    btn4.configure(command=lambda: desligaBotoes(btn2, btn3, btn1))
                                    botaoSalvar.configure(command=lambda : [cadastrarAlt(1, True)])
                                    botaoSalvartxt.bind("<Button-1>", botaoSalvar.cget("command"))

                                case 2:
                                    perguntaAlternativa()
                                    opcao1.insert(ctk.END, i[1])
                                    opcao2.insert(ctk.END, i[2])
                                    opcao3.insert(ctk.END, i[3])
                                    opcao4.insert(ctk.END, i[4])

                                    for x in blist:
                                        digitos = [int(digito) for digito in str(i[5] )]
                                        if x._onvalue in digitos:
                                            x.select()

                                    btn1.configure(command=None)
                                    btn2.configure(command=None) 
                                    btn3.configure(command=None)
                                    btn4.configure(command=None)
                                    botaoSalvar.configure(command=lambda : [cadastrarAlt(2, True)])
                                    botaoSalvartxt.bind("<Button-1>", botaoSalvar.cget("command"))

                                case 3:
                                    perguntaVerdadeiro()

                                    if i[5] == 1:
                                        btn1.select()
                                    else:
                                        btn2.select()

                                    btn1.configure(command=lambda: desligaBotoes(btn2))
                                    btn2.configure(command=lambda: desligaBotoes(btn1))
                                    botaoSalvar.configure(command=lambda : [cadastrarVerdadeiro(True)])
                                    botaoSalvartxt.bind("<Button-1>", botaoSalvar.cget("command"))

                                case 4:
                                    perguntaR()

                                    resposta.insert(ctk.END, i[1])

                                    botaoSalvar.configure(command=lambda : [cadastrarRes(True)])
                                    botaoSalvartxt.bind("<Button-1>", botaoCadastra.cget("command"))

                botaoSalvar = Button(
                    master=frameQuestoes,
                    image=botao_image,
                    borderwidth=0,
                    highlightthickness=0,
                    bg = "#272727",
                    activebackground='#272727',
                    relief="flat"
                )
                botaoSalvar.place(
                    x=969.0,
                    y=15.0,
                    width=283.0,
                    height=82.0
                )

                botaoSalvartxt = ctk.CTkLabel(frameQuestoes,text="Salvar", font=("Consolas", 40), text_color="#FFE873", bg_color="#306998")
                botaoSalvartxt.place(x=1045.0,y=32.0)

                botaoLixo = Button(
                    master=frameQuestoes,
                    image=botaoLixoimg,
                    borderwidth=0,
                    highlightthickness=0,
                    bg = "#272727",
                    activebackground='#272727',
                    state='disabled',
                    command=lambda : deletarQuestao(botaoLixo),
                    relief="flat"
                )                   
                botaoLixo.place(
                    x=50.0,
                    y=650.0,
                    width=48.0,
                    height=48.0
                )

                opcao = ctk.StringVar()

                perguntasBox = ctk.CTkComboBox(frameQuestoes,width=270,font=("Consolas", 20), dropdown_font=("Consolas", 20), variable=opcao, state="readonly")
                perguntasBox.place(relx=0.4, rely=0.04)

                opcao.trace("w",mudouPergunta)

                listaPerguntas = []
                for i in perguntas:
                    listaPerguntas.append(i[0])

                perguntasBox.configure(values=listaPerguntas)

            if criar:
                def mudouOpcao(*args):
                    
                    retiraWidget()
                    desligaBotoes(btn1, btn2, btn3, btn4)
                    limpaText(pergunta, opcao1, opcao2, opcao3, opcao4, resposta)

                    match(tipo.get()):
                        case "Alternativa":
                            perguntaAlternativa()
                            btn1.configure(command=lambda: desligaBotoes(btn2, btn3, btn4))
                            btn2.configure(command=lambda: desligaBotoes(btn1, btn3, btn4)) 
                            btn3.configure(command=lambda: desligaBotoes(btn2, btn1, btn4))
                            btn4.configure(command=lambda: desligaBotoes(btn2, btn3, btn1))
                            botaoCadastra.configure(command=lambda : [check(1)])
                            botaoCadastraText.bind("<Button-1>", botaoCadastra.cget("command"))

                        case "Resposta múltipla":
                            perguntaAlternativa()
                            btn1.configure(command=None)
                            btn2.configure(command=None) 
                            btn3.configure(command=None)
                            btn4.configure(command=None)
                            botaoCadastra.configure(command=lambda : [check(2)])
                            botaoCadastraText.bind("<Button-1>", botaoCadastra.cget("command"))

                        case "Verdadeiro ou Falso":
                            perguntaVerdadeiro()
                            btn1.configure(command=lambda: desligaBotoes(btn2))
                            btn2.configure(command=lambda: desligaBotoes(btn1))
                            botaoCadastra.configure(command=lambda : [check(3)])
                            botaoCadastraText.bind("<Button-1>", botaoCadastra.cget("command"))

                        case "Resposta Curta":
                            perguntaR()
                            botaoCadastra.configure(command=lambda : [check(4)])
                            botaoCadastraText.bind("<Button-1>", botaoCadastra.cget("command"))

                botaoCadastra = Button(
                    master=frameQuestoes,
                    image=botao_image,
                    borderwidth=0,
                    highlightthickness=0,
                    bg = "#272727",
                    activebackground='#272727',
                    relief="flat"
                )
                botaoCadastra.place(
                    x=969.0,
                    y=15.0,
                    width=283.0,
                    height=82.0
                )

                botaoCadastraText = ctk.CTkLabel(frameQuestoes,text="Cadastrar", font=("Consolas", 35), text_color="#FFE873", bg_color="#306998")
                botaoCadastraText.place(x=1025.0,y=35.0)

                opcao = ctk.StringVar()

                tipo = ctk.CTkComboBox(frameQuestoes,width=270,font=("Consolas", 20), dropdown_font=("Consolas", 20), values=["Alternativa", "Resposta múltipla", "Verdadeiro ou Falso","Resposta Curta"], state="readonly", variable=opcao)
                tipo.place(relx=0.4, rely=0.04)
                tipo.set("Alternativa")

                mudouOpcao()
                opcao.trace("w",mudouOpcao)
            else:
                editarInter()
                
        def animacao():
            frameLogin.pack_forget()
            frameLogin2.pack_forget()
            def move(texto, duracao):
                t0 = time.time()
                while True:
                    tempo_decorrido = time.time() - t0
                    if tempo_decorrido >= duracao:
                        break
                    t = tempo_decorrido / duracao

                    valorx = np.interp(t, [0, 1], [float(texto.place_info()["relx"]), 0.123])
                    valory = np.interp(t, [0, 1], [float(texto.place_info()["rely"]), 0.09])

                    if float(texto.place_info()["rely"]) < 0.092:
                        valorx = 0.123
                        valory = 0.09
                        texto.place(relx=valorx, rely=valory, anchor=ctk.CENTER)
                        janela.update()
                        break

                    texto.place(relx=valorx, rely=valory, anchor=ctk.CENTER)
                    janela.update()
                    time.sleep(0.01)
                    
            def type(t):
                txt = ""

                texto = ctk.CTkLabel(janela, text="|",font=("Consolas", 36 * -1))
                texto.place(relx = 0.5, rely=0.5, anchor=ctk.CENTER)
                for i in range(3):
                    texto.configure(text="")
                    janela.update()
                    time.sleep(0.5)
                    texto.configure(text="|")
                    janela.update()
                    time.sleep(0.5)
                    i+=1

                texto.configure(text=txt+"|")
                for char in t:
                    txt += char
                    texto.configure(text=txt+"|")
                    janela.update()
                    time.sleep(0.15)
                texto.configure(text=txt)
                texto.place(relx = 0.495, rely=0.5, anchor=ctk.CENTER)
                janela.update()
                time.sleep(0.3)
                move(texto, 20)
                texto.destroy()
                menu()

            type("print(\"Quiz\")")
            pass

        def menu():
            frameLogin.pack_forget()
            frameLogin2.pack_forget()

            global frameMenu
            frameMenu = ctk.CTkFrame(master=janela,width=1280,height=720)
            frameMenu.pack()

            canvasMenuQuiz = Canvas(
                frameMenu,
                bg = "#272727",
                height = 720,
                width = 974,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasMenuResultados = Canvas(
                frameMenu,
                bg = "#272727",
                height = 720,
                width = 974,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasMenuQuestoes = Canvas(
                frameMenu,
                bg = "#272727",
                height = 720,
                width = 974,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas = Canvas(
                frameMenu,
                bg = "#272727",
                height = 720,
                width = 306.0,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)

            def sairMenu():
                frameMenu.pack_forget()
                canvas.place_forget()
                canvasMenuQuiz.place_forget()
                canvasMenuQuestoes.place_forget()
                canvasMenuResultados.place_forget()
                frameLogin.pack()
                frameLogin2.pack()

            def menuQuiz():
                canvasMenuQuiz.place(x = 306, y = 0)

                canvasMenuResultados.place_forget()
                canvasMenuQuestoes.place_forget()

                canvasMenuQuiz.create_rectangle(
                    0.0,
                    0.0,
                    1280.0,
                    720.0,
                    fill="#383838",
                    outline="")
                
                botaoquiz.configure(image=botaoquiz_image)
                botaoquiztxt.configure(bg_color="#363636", text_color="#306998")

                botaoResultados.configure(image=botaoResultados_image)
                botaoResultadostxt.configure(bg_color="#2F2F2F", text_color="#FFE873")

                buttonquestoes.configure(image=botaoResultados_image)
                buttonquestoestxt.configure(bg_color="#2F2F2F",text_color="#FFE873")

                botaoiniciar.place(
                    x=699,
                    y=626,
                    width=250.0,
                    height=70.0
                )

                botaoiniciartxt.place(x=744,y=636)
                regrasQuiz.place(x=61.0,y=139.0)
                quizTxt.place(x=404.0, y=39.0)


            def menuResultados():
                canvasMenuResultados.place(x = 306, y = 0)
                
                canvasMenuQuiz.place_forget()
                canvasMenuQuestoes.place_forget()

                canvasMenuResultados.create_rectangle(
                    0.0,
                    0.0,
                    1280.0,
                    720.0,
                    fill="#383838",
                    outline="")

                botaoquiz.configure(image=botaoResultados_image)
                botaoquiztxt.configure(bg_color="#2F2F2F", text_color="#FFE873")

                botaoResultados.configure(image=botaoquiz_image)
                botaoResultadostxt.configure(bg_color="#363636", text_color="#306998")

                buttonquestoes.configure(image=botaoResultados_image)
                buttonquestoestxt.configure(bg_color="#2F2F2F",text_color="#FFE873")

            def menuQuestoes():
                canvasMenuQuestoes.place(x = 306, y = 0)
                
                canvasMenuQuiz.place_forget()
                canvasMenuResultados.place_forget()

                canvasMenuQuestoes.create_rectangle(
                    0.0,
                    0.0,
                    1280.0,
                    720.0,
                    fill="#383838",
                    outline="")

                botaoquiz.configure(image=botaoResultados_image)
                botaoquiztxt.configure(bg_color="#2F2F2F", text_color="#FFE873")

                botaoResultados.configure(image=botaoResultados_image)
                botaoResultadostxt.configure(bg_color="#2F2F2F", text_color="#FFE873")

                buttonquestoes.configure(image=botaoquiz_image)
                buttonquestoestxt.configure(bg_color="#363636", text_color="#306998")

            botaoiniciar = Button(
                master= canvasMenuQuiz,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: quiz(),
                relief="flat"
            )
            
            botaoiniciartxt = ctk.CTkLabel(canvasMenuQuiz,text="Iniciar", font=("Consolas", 40), text_color="#FFE873", bg_color="#306998")

            botaoiniciartxt.bind("<Button-1>", botaoiniciar.cget("command"))

            botaoquiz_image = PhotoImage(
            file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_4.png")))

            botaoResultados_image = PhotoImage(
            file=(r"{}\assets\{}".format(OUTPUT_PATH,"button_un.png")))

            botaoquiz = Button(
                master= frameMenu,
                image=botaoquiz_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: menuQuiz(),
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
            
            botaoResultados = Button(
                master= frameMenu,
                image=botaoResultados_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: menuResultados(),
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
                command=lambda: menuQuestoes(),
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
                command=lambda: sairMenu(),
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

            printQuiz = ctk.CTkLabel(frameMenu,text="print(“Quiz”)", font=("Consolas", 36 * -1), text_color="white", fg_color="#272727")
            printQuiz.place(x=28.0, y=40.0)

            quizTxt = ctk.CTkLabel(canvasMenuQuiz,text="Quiz", font=("Consolas", 64), text_color="white", fg_color="#383838")

            regrasQuiz = Label(
                master=canvasMenuQuiz,
                justify="left",
                background="#383838",
                foreground="white",
                text="Tutorial:\n\n● O Quiz apresentará as questões em ordem aleatória.\n\n● Seu tempo será cronometrado, mas não será salvo no sistema.\n\n● As questões podem variar de alternativa, resposta múltipla, \n\nverdadeiro ou falso e resposta curta.\n\n● Após inserir a sua resposta, clique em próxima questão.\n\n● Quando tiver respondido todas as questões, clique em\n\n “Finalizar Quiz”.",
                font=("Consolas", 25 * -1))

            #Menu questões
            botaoTelaQuestoes = Button(
                master= canvasMenuQuestoes,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: telaQuestoes(True),
                relief="flat"
            )

            botaoTelaQuestoestxt = ctk.CTkLabel(canvasMenuQuestoes,text="Criar Questão", font=("Consolas", 28), text_color="#FFE873", bg_color="#306998")

            semPermtxt = ctk.CTkLabel(canvasMenuQuestoes,text="*Você não possui permição para gerenciar.", font=("Consolas", 20), text_color="Grey", bg_color="#383838")
            parabenstxt = ctk.CTkLabel(canvasMenuQuestoes,text="Parabéns!", font=("Consolas", 30), text_color="white", bg_color="#383838")

            gerenciarQuestoestxt = ctk.CTkLabel(canvasMenuQuestoes,text="Gerenciar Questões", font=("Consolas", 45), text_color="white", fg_color="#383838")
            gerenciarQuestoestxt.place(x=265.0, y=50.0)

            telaQuestoesExpl = Label(
                master=canvasMenuQuestoes,
                justify="left",
                background="#383838",
                foreground="white",
                text="● Nesta aba, você pode gerenciar as questões, apenas clique\n\nno botão apropriado e será redirecionado.\n\n● Alunos que responderem o questionário em 100%, poderão\n\nsolicitar questões. Assim que conseguirem, o botão \n\n\"Criar Questões\" será liberado.\n\n● De forma alguma, os alunos poderam consultar\editar \n\nquestões existentes.",
                font=("Consolas", 25 * -1))
            telaQuestoesExpl.place(x=61.0,y=160.0)

            botaoTelaEditarQuestoes = Button(
                master= canvasMenuQuestoes,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: telaQuestoes(False),
                relief="flat"
            )

            botaoTelaEditarQuestoestxt = ctk.CTkLabel(canvasMenuQuestoes,text="Editar Questões", font=("Consolas", 27), text_color="#FFE873", bg_color="#306998")

            if score == scoreMax:
                botaoTelaQuestoes.place(
                    x=699,
                    y=626,
                    width=250.0,
                    height=70.0
                )
                botaoTelaQuestoestxt.place(x=728,y=645)
                parabenstxt.place(x=750,y=580)
            elif admin == 0:
                semPermtxt.place(x=250,y=630)

            if admin == 1:
                botaoTelaQuestoes.place(
                        x=699,
                        y=626,
                        width=250.0,
                        height=70.0
                    )
                botaoTelaQuestoestxt.place(x=728,y=645)
                botaoTelaEditarQuestoes.place(
                    x=25,
                    y=626,
                    width=250.0,
                    height=70.0
                )
                botaoTelaEditarQuestoestxt.place(x=38,y=645)

            #Menu resultados

            botaoTelaResultados = Button(
                master= canvasMenuResultados,
                image=botao_image,
                borderwidth=0,
                highlightthickness=0,
                bg = "#383838",
                activebackground='#383838',
                command=lambda: telaResultados(),
                relief="flat"
            )
            botaoTelaResultados.place(
                    x=699,
                    y=626,
                    width=250.0,
                    height=70.0
            )
            
            botaoTelaResultadostxt = ctk.CTkLabel(canvasMenuResultados,text="Ver Resultados", font=("Consolas", 26), text_color="#FFE873", bg_color="#306998")
            botaoTelaResultadostxt.place(x=725,y=647)

            verResultadostxt = ctk.CTkLabel(canvasMenuResultados,text="Resultados", font=("Consolas", 53), text_color="white", fg_color="#383838")
            verResultadostxt.place(x=350.0, y=50.0)

            telaResultadosExpl = Label(
                master=canvasMenuResultados,
                justify="left",
                background="#383838",
                foreground="white",
                text="● Aqui você pode ver os seus resultados, apenas clique no botão \n\ne será redirecionado.\n\n● As suas tentativas são mostradas em ordem, e disponibilizam\n\na quantidade de acertos em cada tentativa.",
                font=("Consolas", 25 * -1))
            telaResultadosExpl.place(x=61.0,y=160.0)

            botaoLista = [botaoiniciar, botaoquiz, botaoResultados,buttonquestoes, botaoTelaQuestoes, botaoTelaResultados, botaoTelaEditarQuestoes]
            textoLista = [botaoiniciartxt, botaoquiztxt, botaoResultadostxt, buttonquestoestxt, botaoTelaQuestoestxt, botaoTelaResultadostxt, botaoTelaEditarQuestoestxt]
            conta = 0

            for i in textoLista:
                i.bind("<Button-1>", botaoLista[conta].cget("command"))
                #ativar clique botao quando clicar no texto
                conta += 1

            menuQuiz()

            janela.resizable(False, False)
            janela.mainloop()
            
        con = mysql.connector.connect(host='localhost', database='users', user='root', password='mysqlimt')
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
                consulta = (F"select RA FROM usuarios;")  
                cursor.execute(consulta)
                
                puxa = list(cursor.fetchall())

                consultaSenha = (f"select password FROM usuarios;") 
                cursor.execute(consultaSenha)

                puxaSenha = list(cursor.fetchall())
                
                for ra in puxa:
                    if str(ra) != "('',)" and str(ra) == "('{}',)".format(self.usuarioEntry):
                         for senha in puxaSenha:
                            if str(senha) != "('',)" and str(senha) == "('{}',)".format(self.senhaEntry):
                                raAdap = str(ra).strip("(),' ")
                                cursor.execute(f"select eadmin FROM usuarios WHERE RA = \"{raAdap}\"")
                                global admin
                                admin = int(str(cursor.fetchall()).strip("(),[]"))
                                animacao()
                            else:
                                print('erro')        
                else:
                    erroBox = messagebox.showwarning(title="Aviso",message="Erro, seus dados não conferem")
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
            cadastroLabel=ctk.CTkLabel(master=frameCadastro, text="Caso seu cadastro seja registrado uma mensagem automatica será exibida", text_color="green",font=("Roboto",10)).place(x=90, y=330)
            
            def back():
                frameCadastro.pack_forget()
                frameLogin.pack(side=RIGHT)
                frameLogin2.pack_forget()
                frameLogin2.pack(side=RIGHT)

            save_Button = ctk.CTkButton(master=frameCadastro, text="REGISTRAR",width=145, fg_color="green",hover_color="#014B05",command=lambda:  (self.cadastrarUsuario(NomeEntry.get(),RAEntry.get(),senhaEntry.get())))
            save_Button.place(x=275,y=385)

            voltarButton = ctk.CTkButton(master=frameCadastro, text="Voltar",width=145,command=back, fg_color="gray", hover_color="#696969")
            voltarButton.place(x=85, y=385)

        registerButton = ctk.CTkButton(master=frameLogin, text="REGISTER", width=150,fg_color="green", hover_color="#2d9334",command= telaCadastro)
        registerButton.place(x=250,y=385)

        return frameLogin
        
Application()

janela.mainloop()