
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug,post,get,request



from csv import reader

contents = []
input_file = open("data.csv", "r")
for row in reader(input_file):
    contents = contents + [row]

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-9" />
                <title>%s</title>
                <style>
                input[type="submit"]{
                
                    color:red;
                    text-shodow:3px 3px 2px red;
                    background-color:lightblue;
                    }
                    
                select{
                padding-top:3px;
                padding-bottom :3px;
                border-style:solid;
                background-color:lightblue:
                }
                html{
                
                background-color:lightgrey;
                }
               
                table,th,td{
                
                    padding-top:50px;
                    padding-bottom:25px;
                    border: 1px solid black;
                    text-align:center;
                    table-layout:initial;
                    background-color: #f1f1c1;
                
                }
                
                
                
                
                
                
                
                
                
                
            </style>
            </head>
            <body>
            
            %s
            </body>
        </html>

    """ % (title,text)
    return page


@get('/')
def login():
    return '''


        <form action="/" method="POST">                          
            user_name: <input name="uname"  type="text"  />
            password: <input name="pname"  type="password" />
            <input type="submit" value="Login" />    

        </form>
    '''




@post('/')
def login():
    user_name = request.forms.get('uname')
    password = request.forms.get('pname')
    if user_name == "emre" and password == "1234":
        return index()


def index():

    text="""<form action="/home" method="GET">
	<select name="province">
	<option value="adana">Adana</option>
	<option value="adiyaman">Adiyaman</option>
	<option value="afyonkarahisar">Afyonkarahisar</option>
	<option value="agri">Agri</option>
	<option value="amasya">Amasya</option>
	<option value="ankara">Ankara</option>
	<option value="antalya">Antalya</option>
	<option value="artvin">Artvin</option>
	<option value="aydin">Aydin</option>
	<option value="balikesir">Balikesir</option>
	<option value="bilecik">Bilecik</option>
	<option value="bingol">Bingol</option>
	<option value="bitlis">Bitlis</option>
	<option value="bolu">Bolu</option>
	<option value="burdur">Burdur</option>
	<option value="bursa">Bursa</option>
	<option value="canakkale">canakkale</option>
	<option value="cankiri">cankiri</option>
	<option value="corum">corum</option>
	<option value="denizli">Denizli</option>
	<option value="diyarbakir">Diyarbakir</option>
	<option value="edirne">Edirne</option>
	<option value="elazig">Elazig</option>
	<option value="erzincan">Erzincan</option>
	<option value="erzurum">Erzurum</option>
	<option value="eskisehir">Eskisehir</option>
	<option value="gaziantep">Gaziantep</option>
	<option value="giresun">Giresun</option>
	<option value="gumushane">Gumushane</option>
	<option value="hakkari">Hakkari</option>
	<option value="hatay">Hatay</option>
	<option value="isparta">isparta</option>
	<option value="mersin">Mersin</option>
	<option value="istanbul">İstanbul</option>
	<option value="izmir">İzmir</option>
	<option value="kars">Kars</option>
	<option value="kastamonu">Kastamonu</option>
	<option value="kayseri">Kayseri</option>
	<option value="kirsehir">Kirsehir</option>
	<option value="kocaeli">Kocaeli</option>
	<option value="konya">Konya</option>
	<option value="kutahya">Kutahya</option>
	<option value="malatya">Malatya</option>
	<option value="manisa">Manisa</option>
	<option value="kahramanmaras">Kahramanmaras</option>
	<option value="mardin">Mardin</option>
	<option value="mugla">Mugla</option>
	<option value="mus">Mus</option>
	<option value="nevsehir">Nevsehir</option>
	<option value="nigde">Nigde</option>
	<option value="ordu">Ordu</option>
	<option value="rize">Rize</option>
	<option value="sakarya">Sakarya</option>
	<option value="samsun">Samsun</option>
	<option value="siirt">Siirt</option>
	<option value="sinop">Sinop</option>
	<option value="sivas">Sivas</option>
	<option value="tekirdag">Tekirdag</option>
	<option value="tokat">Tokat</option>
	<option value="trabzon">Trabzon</option>
	<option value="tunceli">Tunceli</option>
	<option value="sanlıurfa">sanlıurfa</option>
	<option value="usak">Usak</option>
	<option value="van">Van</option>
	<option value="yozgat">Yozgat</option>
	<option value="zonguldak">Zonguldak</option>
	<option value="aksaray">Aksaray</option>
	<option value="bayburt">Bayburt</option>
	<option value="karaman">Karaman</option>
	<option value="kirikkale">Kirikkale</option>	
	<option value="batman">Batman</option>
	<option value="sirnak">sirnak</option>
	<option value="bartin">Bartin</option>
	<option value="agri">Ardahan</option>
	<option value="igdir">İgdir</option>
	<option value="yalova">Yalova</option>
	<option value="karabük">Karabuk</option>
	<option value="kilis">Kilis</option>
	<option value="osmaniye">Osmaniye</option>
	<option value="duzce">Duzce</option>

	
	
	
	
	
	</select>
	<input type="submit" value="Submit">
	</form>"""

    return htmlify("home",text)
def home():

    global contents

    sec=request.GET["province"]

    tab ="""
    
        <table>
            <tr>
                <th><h1>province</h1></th>
                <th><h1>total population</h1></th>
                <th><h1>İn-migration</h1></th>
                <th><h1>Out-migration</h1></th>
                <th><h1>Net-migration</h1></th>
                <th>"""
    if sec=="adana":
       # tab +=contents[0][0]+"</th></tr>"
        for i in range(5):
            tab +="<tr>"
            for j in range(5):
                tab +="<td>"+ contents[0][j]+"</td>"
            tab +="</tr>"
            return htmlify(contents[0][1],tab)
    elif sec=="adiyaman":
        for i in range(5):
            tab +="<tr>"
            for j in range(5):
                tab +="<td>"+ contents[1][j]+"</td>"
            tab +="</tr>"
            return htmlify(contents[1][1],tab)

    elif sec == "afyonkarahisar":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[2][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[2][1], tab)

    elif sec == "agri":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[3][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[3][1], tab)
    elif sec == "amasya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[4][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[4][1], tab)
    elif sec == "ankara":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[5][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[5][1], tab)
    elif sec == "antalya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[6][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[6][1], tab)
    elif sec == "artvin":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[7][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[7][1], tab)
    elif sec == "aydin":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[8][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[8][1], tab)
    elif sec == "balikesir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[9][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[9][1], tab)
    elif sec == "bilecik":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[10][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[10][1], tab)
    elif sec == "bingol":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[11][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[11][1], tab)
    elif sec == "bitlis":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[12][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[12][1], tab)
    elif sec == "bolu":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[13][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[13][1], tab)
    elif sec == "burdur":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[14][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[14][1], tab)
    elif sec == "bursa":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[15][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[15][1], tab)
    elif sec == "canakkale":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[16][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[16][1], tab)
    elif sec == "cankiri":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[17][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[17][1], tab)
    elif sec == "corum":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[18][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[18][1], tab)
    elif sec == "denizli":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[19][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[19][1], tab)
    elif sec == "diyarbakir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[20][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[20][1], tab)
    elif sec == "edirne":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[21][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[21][1], tab)
    elif sec == "elazig":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[22][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[22][1], tab)
    elif sec == "erzincan":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[23][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[23][1], tab)
    elif sec == "erzurum":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[24][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[24][1], tab)
    elif sec == "eskisehir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[25][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[25][1], tab)
    elif sec == "gaziantep":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[26][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[26][1], tab)
    elif sec == "giresun":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[27][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[27][1], tab)
    elif sec == "gumushane":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[28][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[28][1], tab)
    elif sec == "hakkari":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[29][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[29][1], tab)
    elif sec == "hatay":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[30][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[30][1], tab)
    elif sec == "isparta":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[31][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[31][1], tab)
    elif sec == "mersin":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[32][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[32][1], tab)
    elif sec == "istanbul":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[33][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[33][1], tab)
    elif sec == "izmir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[34][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[34][1], tab)
    elif sec == "kars":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[35][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[35][1], tab)
    elif sec == "kastamonu":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[36][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[36][1], tab)
    elif sec == "kayseri":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[37][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[37][1], tab)
    elif sec == "kirsehir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[38][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[38][1], tab)
    elif sec == "kocaeli":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[39][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[39][1], tab)
    elif sec == "konya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[40][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[40][1], tab)
    elif sec == "kutahya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[41][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[41][1], tab)
    elif sec == "malatya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[42][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[42][1], tab)
    elif sec == "manisa":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[43][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[43][1], tab)
    elif sec == "kahramanmaras":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[44][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[44][1], tab)
    elif sec == "mardin":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[45][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[45][1], tab)
    elif sec == "mugla":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[46][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[46][1], tab)
    elif sec == "mus":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[47][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[47][1], tab)
    elif sec == "munevsehir":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[48][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[48][1], tab)
    elif sec == "nigde":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[49][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[49][1], tab)
    elif sec == "ordu":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[50][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[50][1], tab)
    elif sec == "rize":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[51][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[51][1], tab)
    elif sec == "sakarya":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[52][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[52][1], tab)
    elif sec == "samsun":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[53][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[53][1], tab)
    elif sec == "siirt":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[54][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[54][1], tab)
    elif sec == "sinop":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[55][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[55][1], tab)
    elif sec == "sivas":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[56][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[56][1], tab)
    elif sec == "tekirdag":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[57][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[57][1], tab)
    elif sec == "tokat":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[58][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[58][1], tab)
    elif sec == "trabzon":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[59][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[59][1], tab)
    elif sec == "tunceli":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[60][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[60][1], tab)
    elif sec == "sanlıurfa":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[61][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[61][1], tab)
    elif sec == "usak":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[62][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[62][1], tab)
    elif sec == "van":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[63][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[63][1], tab)
    elif sec == "yozgat":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[64][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[64][1], tab)
    elif sec == "zonguldak":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[65][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[65][1], tab)
    elif sec == "aksaray":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[66][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[66][1], tab)
    elif sec == "bayburt":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[67][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[67][1], tab)
    elif sec == "karaman":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[68][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[68][1], tab)
    elif sec == "kirikkale":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[69][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[69][1], tab)
    elif sec == "batman":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[70][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[70][1], tab)
    elif sec == "sirnak":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[71][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[71][1], tab)
    elif sec == "bartin":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[72][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[72][1], tab)
    elif sec == "ardahan":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[73][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[73][1], tab)
    elif sec == "ıgdır":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[74][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[74][1], tab)
    elif sec == "yalova":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[75][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[75][1], tab)
    elif sec == "karabuk":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[76][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[76][1], tab)
    elif sec == "kilis":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[77][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[77][1], tab)
    elif sec == "osmaniye":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[78][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[78][1], tab)
    elif sec == "duzce":
        for i in range(5):
            tab += "<tr>"
            for j in range(5):
                tab += "<td>" + contents[79][j] + "</td>"
            tab += "</tr>"
            return htmlify(contents[79][1], tab)



route('/', 'GET',)
route('/index','GET',index)
route('/home','GET',home)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

