#これをGitHub経由でオンラインからフォームを送信できるようにしたい

from flask import Flask, request,render_template

app = Flask(__name__)

# login処理です
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        #ここで送られてきた値が各名前変数に格納されている
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))

        print("マグロの数:" + str(request.form['maguro']) + "つの注文を承りました。")
        print("マグロの握りを処理します")
        print("ウニの数:" + str(request.form['uni']) + "つの注文を承りました。")
        print("ウニの握りを処理します")
        print("エビの数:" + str(request.form['ebi']) + "つの注文を承りました。")
        print("エビの握りを処理します")
        print("玉子の数:" + str(request.form['tamago']) + "つの注文を承りました。")
        print("玉子の握りを処理します")
        print("イクラの数:" + str(request.form['ikura']) + "つの注文を承りました。")
        print("イクラの握りを処理します")
        print("イカの数:" + str(request.form['ika']) + "つの注文を承りました。")
        print("イカの握りを処理します")
        
        maguro = request.form['maguro']  
        uni = request.form['uni'] 
        ebi = request.form['ebi'] 
        tamago = request.form['tamago'] 
        ikura = request.form['ikura'] 
        ika = request.form['ika'] 

        maguro = int(maguro)
        uni = int(uni)
        ebi = int(ebi)
        tamago = int(tamago)
        ikura = int(ikura)
        ika = int(ika)

        print(type(maguro))
        for w in range(maguro , uni * 4):
             print(w)
        print(str(uni))
        print(str(ikura))
        print(str(ika))
        print(str(uni))

        return render_template('form.html')
         
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8000, debug=True)