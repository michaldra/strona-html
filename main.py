from flask import Flask, render_template
import random 

app = Flask(__name__)

facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.","Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.","Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.","Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.","Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.","Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.","Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.","Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi."]
coin_outcomes = ["Orzeł","Reszka"]
letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*-_=+;:,./?"

def gen_password():
    haslo = ""
    for i in range(12):
        haslo = haslo + letters[random.randint(0,len(letters)-1)]
    return haslo

@app.route("/")
def main():
    return "<h1>Cześć! Witaj na mojej stronie!</h1><h2><a href='/stara_strona'>Stary wygląd strony</a></h2><h2><a href='/random_fact'>Zobacz losowy fakt na temat zależności technologicznych</a></h2><h2><a href='/coin_flip'>Rzuć monetą</a></h2><h2><a href='/password_generator'>Wygeneruj losowe hasło</a></h2>"

@app.route("/random_fact")
def fact():
    return f"<p>{random.choice(facts_list)}</p><br><p><a href='/random_fact'>Nowy fakt</a></p><h4><a href='/'>Powrót</a></h4>"

@app.route("/coin_flip")
def coin():
    return f"<h3>{random.choice(coin_outcomes)}</h3><br><p><a href='/coin_flip'>Rzuć jeszcze raz</a></p><h4><a href='/'>Powrót</a></h4>"

@app.route("/password_generator")
def password():
    return f"<h3>Wygenerowane hasło: {gen_password()}</h3><br><p><a href='/password_generator'>Wygeneruj nowe hasło</a></p><h4><a href='/'>Powrót</a></h4>"

@app.route("/stara_strona")
def strona():
    return render_template("index.html")

app.run(debug=True)