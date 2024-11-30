import streamlit as st
import sympy as sy
import math as mt

st.set_page_config(
    page_title="Aplikasi Trigonometri",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
kolom = st.columns(2)
kolom[0].image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Circle_cos_sin.gif",width=300)
kolom[1].image("https://i.gifer.com/origin/57/57df9428b0c191201e7ce06f4a2e717c_w200.gif",width=200)
st.title("Trigonometri")

tab1,tab2,tab3= st.tabs(["Penjumlahan Sudut","Identitas Ganda","Penjumlahan Fungsi Trigonometri"])
with tab1:
    koloman = st.columns(2)
    koloman[0].image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732954776/pengurangan_sudut_cos_tx9wsz.png")
    koloman[1].image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732956474/pengurangan_sudut_sin_hel6pw.png")
    halaman = st.sidebar.selectbox('untuk penjumlahan sudut',['Pengertian','contoh','latihan'])
    if halaman=="Pengertian":
        st.header("Penjumlahan Sudut")
        st.markdown('''<h4 style="color:green">
Dalam trigonometri, terdapat identitas penjumlahan dan pengurangan sudut yang sering digunakan
untuk menyederhanakan perhitungan. Berikut adalah rumus dasar untuk penjumlahan dan pengurangan sudut: 
               </h4>''', unsafe_allow_html=True)
        st.markdown('''
<h5 style="color:blue">Rumus Sinus Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\sin{(a+b)}=\sin{a}\cos{b}+\cos{a}\sin{b}")
        st.latex("\sin{(a-b)}=\sin{a}\cos{b}-\cos{a}\sin{b}")
        st.markdown('''<h5 style="color:blue">Rumus cosinus Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\cos{(a+b)}=\cos{a}\cos{b}-\sin{a}\sin{b}")
        st.latex("\cos{(a-b)}=\cos{a}\cos{b}+\sin{a}\sin{b}")
        st.markdown('''<h5 style="color:blue">Rumus Tangen Penjumlahan dan Pengurangan</h5>
                ''',unsafe_allow_html=True)
        st.latex("\\tan{(a+b)}=\\frac{\\tan{a}+\\tan{b}}{1-\\tan{a}\\tan{b}},\;dengan\;syarat\;\\tan{a}\\tan{b}\\neq{1}")
        st.latex("\\tan{(a-b)}=\\frac{\\tan{a}-\\tan{b}}{1+\\tan{a}\\tan{b}},\;dengan\;syarat\;\\tan{a}\\tan{b}\\neq{-1}")
        bukti=st.button("lihat pembuktian")
        if bukti:
            kolom1 = st.columns([1,2],vertical_alignment="center")
            with kolom1[0]:
                st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBy-CsA5Cd9NHwWeZ4AgxFCEwk97AneGQfrqFNwV4MgqoLZSoKdVT7INNoBQknFxJmCsxJL1608XYTRzyXfHjbfVXMB30CZX4gRClJqtAp1DD7Osoooc5HB2UR5Q_xwn3lDeoLWr_Nmtw/s320/penurunan+rumus+cos+2.png")
            tulisan_html1='''
                            <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GeoGebra Integration</title>
  <script src="https://cdn.geogebra.org/apps/deployggb.js"></script>
  <style>
      #ggb-container{
          border:2px solid black;
          box-shadow:2px 2px 2px 2px blue;
      }
  </style>
</head>
<body>
  <h1>Bukti Pertama</h1>
  <div><input type="text" id="masukan"><div>
  <div id="ggb-container" style="width: 800px; height: 500px;"></div>
  
  <script>
    var ggbApp = new GGBApplet({
      "id":"ggbApplet",
      "appName": "classic",  // Pilihan: "graphing", "geometry", "3d", "classic", dll.
      "width": 800,
      "height": 500,
      "showToolBar": true,  // Menampilkan toolbar GeoGebra
      "showAlgebraInput": true,  // Menampilkan input aljabar
      "showMenuBar": true,  // Menampilkan menu
    }, true); // 'true' untuk membuat aplikasi GeoGebra responsif

    // Muat aplikasi GeoGebra ke dalam container
    window.addEventListener("load", function () {
      ggbApp.inject('ggb-container');
    });
    var masukan = document.getElementById("masukan")
    
    masukan.addEventListener("keydown",(e)=>{
        if(e.key==="Enter"){
            var pisahkan = masukan.value.split(";")
            ggbApplet.evalCommand('Text("'+pisahkan[0]+'",'+pisahkan[1]+',true,true)')
            
        }
    })
  </script>
</body>
</html>
'''
            with kolom1[1]:
                st.components.v1.html(tulisan_html1,width=800,height=600)
    elif halaman=="contoh":
        st.header("contoh")
        st.subheader("Penjumlahan 2 sudut")
        st.write("Masukan 2 nilai sudut")
        if "bilangan1" not in st.session_state:
            st.session_state.bilangan1=""
        if "bilangan2" not in st.session_state:
            st.session_state.bilangan2=""
        kolom1 = st.columns(2)
        kolom1[0].text_input("Masukan sudut pertama",key="bilangan1")
        kolom1[1].text_input("Masukan sudut kedua",key="bilangan2")
        st.write("harus diisi kedua sudutnya kemudian di enter")
        if st.session_state.bilangan1 and st.session_state.bilangan2:
            nilai1 = int(st.session_state.bilangan1)
            nilai2 = int(st.session_state.bilangan2)
            nilai3 = sy.latex(sy.sin(sy.rad(nilai1)))
            nilai4 = sy.latex(sy.cos(sy.rad(nilai2)))
            nilai5 = sy.latex(sy.cos(sy.rad(nilai1)))
            nilai6 = sy.latex(sy.sin(sy.rad(nilai2)))
            nilai7 = sy.latex(sy.sin(sy.rad(nilai1))*sy.cos(sy.rad(nilai2)))
            nilai8 = sy.latex(sy.cos(sy.rad(nilai1))*sy.sin(sy.rad(nilai2)))
            nilai9 = sy.latex(sy.sin(sy.rad(nilai1))*sy.cos(sy.rad(nilai2))+sy.cos(sy.rad(nilai1))*sy.sin(sy.rad(nilai2)))
            nilai10 = sy.latex(sy.cos(sy.rad(nilai1))*sy.cos(sy.rad(nilai2)))
            nilai11 = sy.latex(sy.sin(sy.rad(nilai1))*sy.sin(sy.rad(nilai2)))
            nilai12 = sy.latex(sy.cos(sy.rad(nilai1))*sy.cos(sy.rad(nilai2))-sy.sin(sy.rad(nilai1))*sy.sin(sy.rad(nilai2)))
            nilai13 = sy.latex(sy.tan(sy.rad(nilai1)))
            nilai14 = sy.latex(sy.tan(sy.rad(nilai2)))
            nilai15 = sy.latex(sy.tan(sy.rad(nilai1))+sy.tan(sy.rad(nilai2)))
            nilai16 = sy.latex(sy.tan(sy.rad(nilai1))*sy.tan(sy.rad(nilai2)))
            nilai17 = sy.latex(1-sy.tan(sy.rad(nilai1))*sy.tan(sy.rad(nilai2)))
            nilai18 = sy.latex((sy.tan(sy.rad(nilai1))+sy.tan(sy.rad(nilai2)))/(1-sy.tan(sy.rad(nilai1))*sy.tan(sy.rad(nilai2))))
            st.latex('\sin{('+str(nilai1)+'+'+str(nilai2)+')}=\sin{'+str(nilai1)+'}\cos{'+str(nilai2)+'}+\cos{'+str(nilai1)+'}\sin{'+str(nilai2)+'}='+nilai3+ \
                     '('+nilai4+')+'+nilai5+'('+nilai6+')='+nilai7+'+'+nilai8+"="+nilai9+'\\'+ \
                     '\\cos{('+str(nilai1)+'+'+str(nilai2)+')}=\cos{'+str(nilai1)+'}\cos{'+str(nilai2)+'}-\sin{'+str(nilai1)+'}\sin{'+str(nilai2)+'}='+nilai4+ \
                     '('+nilai5+')-'+nilai3+'('+nilai6+')='+nilai10+'-'+nilai11+'='+nilai12+'\\'+ \
                     '\\\\tan{('+str(nilai1)+'+'+str(nilai2)+')}=\\frac{\\tan{'+str(nilai1)+'}+\\tan{'+str(nilai2)+'}}{1-(\\tan{'+str(nilai1)+'})(\\tan('+str(nilai2)+ \
                     '))}=\\frac{'+nilai13+'+'+nilai14+'}{1-('+nilai13+')('+nilai14+')}=\\frac{'+nilai15+'}{1-'+nilai16+'}=\\frac{'+nilai15+'}{'+nilai17+'}='+nilai18)
        if "bilangan3" not in st.session_state:
            st.session_state.bilangan3=""
        if "bilangan4" not in st.session_state:
            st.session_state.bilangan4=""
        kolom2 = st.columns(2)
        st.write("Contoh Pengurangan 2 sudut")
        kolom2[0].text_input("Masukan sudut pertama",key="bilangan3")
        kolom2[1].text_input("Masukan sudut kedua",key="bilangan4")
        st.write("harus diisi kedua sudutnya kemudian di enter")
        if st.session_state.bilangan3 and st.session_state.bilangan4:
            nilai19 = int(st.session_state.bilangan3)
            nilai20 = int(st.session_state.bilangan4)
            nilai21 = sy.latex(sy.sin(sy.rad(nilai19)))
            nilai22 = sy.latex(sy.cos(sy.rad(nilai20)))
            nilai23 = sy.latex(sy.cos(sy.rad(nilai19)))
            nilai24 = sy.latex(sy.sin(sy.rad(nilai20)))
            nilai25 = sy.latex(sy.sin(sy.rad(nilai19))*sy.cos(sy.rad(nilai20)))
            nilai26 = sy.latex(sy.cos(sy.rad(nilai19))*sy.sin(sy.rad(nilai20)))
            nilai27 = sy.latex(sy.sin(sy.rad(nilai19))*sy.cos(sy.rad(nilai20))-sy.cos(sy.rad(nilai19))*sy.sin(sy.rad(nilai20)))
            nilai28 = sy.latex(sy.cos(sy.rad(nilai19))*sy.cos(sy.rad(nilai20)))
            nilai29 = sy.latex(sy.sin(sy.rad(nilai19))*sy.sin(sy.rad(nilai20)))
            nilai30 = sy.latex(sy.cos(sy.rad(nilai19))*sy.cos(sy.rad(nilai20))+sy.sin(sy.rad(nilai19))*sy.sin(sy.rad(nilai20)))
            nilai31 = sy.latex(sy.tan(sy.rad(nilai19)))
            nilai32 = sy.latex(sy.tan(sy.rad(nilai20)))
            nilai33 = sy.latex(sy.tan(sy.rad(nilai19))-sy.tan(sy.rad(nilai20)))
            nilai34 = sy.latex(sy.tan(sy.rad(nilai19))*sy.tan(sy.rad(nilai20)))
            nilai35 = sy.latex(1+sy.tan(sy.rad(nilai19))*sy.tan(sy.rad(nilai20)))
            nilai36 = sy.latex((sy.tan(sy.rad(nilai19))-sy.tan(sy.rad(nilai20)))/(1+sy.tan(sy.rad(nilai19))*sy.tan(sy.rad(nilai20))))
            with st.container(border=True):
                st.latex('\sin{('+str(nilai19)+'-'+str(nilai20)+')}=\sin{'+str(nilai19)+'}\cos{'+str(nilai20)+'}-\cos{'+str(nilai19)+'}\sin{'+str(nilai20)+'}='+nilai21+ \
                     '('+nilai22+')-'+nilai23+'('+nilai24+')='+nilai25+'-'+nilai26+"="+nilai27+'\\'+ \
                     '\\\\cos{('+str(nilai19)+'-'+str(nilai20)+')}=\cos{'+str(nilai19)+'}\cos{'+str(nilai20)+'}-\sin{'+str(nilai19)+'}\sin{'+str(nilai20)+'}='+nilai22+ \
                     '('+nilai23+')+'+nilai21+'('+nilai24+')='+nilai28+'+'+nilai29+'='+nilai30+'\\'+ \
                     '\\\\tan{('+str(nilai19)+'-'+str(nilai20)+')}=\\frac{\\tan{'+str(nilai19)+'}-\\tan{'+str(nilai20)+'}}{1+(\\tan{'+str(nilai19)+'})(\\tan('+str(nilai20)+ \
                     '))}=\\frac{'+nilai31+'-'+nilai32+'}{1+('+nilai31+')('+nilai32+')}=\\frac{'+nilai33+'}{1+'+nilai34+'}=\\frac{'+nilai33+'}{'+nilai35+'}='+nilai36)
with tab2:
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732718333/animasi_trig_fet1ii.gif",width=400)
    st.sidebar.selectbox('Sudut Berganda',["Pengertian dan Rumus","contoh","latihan"])
    gaya_css = '''
    <style>
        #judul1{
            font-family:Elephant;
            font-size:30px;
            color:blue;
            text-shadow:2px 2px 2px yellow;
        }
        #paragraf{
            font-family:"comic sans ms";
            font-size:20px;
            font-weight:bold;
            border:2px solid black;
            border-radius:10px;
            background-color:cyan;
            margin:10px;
            padding:5px;
        }
    </style>
    '''
    st.markdown(gaya_css,unsafe_allow_html=True)
    st.markdown("<div id='judul1'>Sudut Berganda</div>",unsafe_allow_html=True)
    st.markdown("""<div id='paragraf'>Sudut berganda dalam trigonometri adalah konsep yang melibatkan perhitungan
trigonometri dengan sudut yang merupakan kelipatan dari sudut tertentu, seperti 2θ, 3θ, dan seterusnya.
Berikut adalah rumus dasar yang sering digunakan untuk sudut berganda:</div>""",unsafe_allow_html=True)
    coba='''
    <html>
    <head>
        <style>
            #bagian{
                font-family:broadway;
                font-size:15px;
                border:2px solid black;
                border-radius:5px;
                padding:3px;
                margin-top:10px;
                background-color:orange;
            }
            .bagian1{
                font-family:"cooper black";
                font-size:14px;
                font-weight:bold;
            }
            ol {
                border-radius:10px;
                background-color:yellow;
                padding:5px;
            }
            .bagian2{
                border-radius:10px;
                background-color:orange;
                padding:5px;
                margin:5px;
            }
        </style>
        <script>
        MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']]
        }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
    </script>
    </head>
    <body>
        <div>
        <div><span id="bagian">Rumus Sudut Berganda</span>
            <ol>
                <li ><span class="bagian1">Rumus Ganda</span></li>
                    <ul class="bagian2" type="a">
                        <li>Sinus Sudut Ganda
                            \[\sin{2\\theta}=2\sin{\\theta}\cos{\\theta}\]
                        </li>
                        <li>Cosinus Sudut Ganda
                             \[\cos{2\\theta}=\cos^{2}{\\theta}-\sin^{2}{\\theta}=2\cos^{2}{\\theta}-1=1-2\sin^{2}{\\theta}\]
                        </li>
                        <li>Tangen Sudut Ganda
                            \[\\tan{2\\theta}=\\frac{\\tan^{2}{\\theta}}{1-\\tan^{2}{\\theta}}\\;dengan\\;syarat\\tan{\\theta}\\neq{\pm{1}}\]
                        </li>
                    </ul>
                <li >
                    <span class="bagian1">Rumus Sudut Tiga Kali Triple Angle</span>
                    <ul class="bagian2" type="a">
                        <li>Sinus Sudut Tiga Kali
                            \[\sin{3\\theta}=3\sin{\\theta}-4\sin^{3}{\\theta}\]
                        </li>
                        <li>Cosinus Sudut Ganda
                             \[\cos{3\\theta}=4\cos^{3}{\\theta}-3\cos{\\theta}\]
                        </li>
                        <li>Tangen Sudut Ganda
                            \[\\tan{3\\theta}=\\frac{3\\tan{\\theta}-4\\tan^{3}{\\theta}}{1-3\\tan^{2}{\\theta}}\\;dengan\\;syarat\\;1-\\tan^{3}{\\theta}\\neq{0}\]
                        </li>
                    </ul>
                </li>
            </ol>
        </div>
        <div></div>
    </div>
    </body>
    </html>

    '''
    st.components.v1.html(coba,height=1200)


        
