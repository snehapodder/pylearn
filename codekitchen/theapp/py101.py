import streamlit as st
from streamlit_embedcode import github_gist

def codearea():
    st.markdown("""
    *Try writing your own codes in Google Colab notebooks 👉 *
    <a href="https://colab.research.google.com/" target="_blank"><img width="64" height="64" src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Github" > </a>
    
    """, unsafe_allow_html=True)

def first():
    st.subheader("First things first")
    st.markdown("""
    In order to code, you will need of course, the language itself.  First, let us get our programming languages installed and set up in our systems. To install and get started with python, simply follow the steps here -  \n
    Python documentation - [https://docs.python.org/3/](https://docs.python.org/3/)
    
    Now, we will need an **[Integrated development environment  (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)** for writing and executing our codes
    There are numerous options available. Few of the commonly used are -
    * [Visual Studio Code ](https://code.visualstudio.com/)
    * [Atom Code Editor ] (https://atom.io/)
    * [PyCharm] (https://www.jetbrains.com/pycharm/)
    * [R Studio](https://www.rstudio.com/products/rstudio/download/) - recommended for coding in R but also supports python 😉
    * [Jupyter Notebook] (https://jupyter.org/)
    💡 Having issues with the above? Try **[Google Colab](https://colab.research.google.com/) **
    """,  unsafe_allow_html=True)

def helloworld():
    st.subheader("**The famous hello-world program 😎**")
    st.markdown("""
    Welcome to the world of python. In this section, we simply print a string using python code. You can say it's kind of a ritual/tradition for anyone who sets on a journey in coding with any language - our way of saying "Hey world, here I come!" 😉  
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=print%28%27Hello%2520World%21%21%27%29%250Aprint%28%27Get%2520ready%2520to%2520rock-N-roll%2520%27%29%250A%2523%2520we%2520saw%2520that%2520the%2520lines%2520automatically%2520shifted%2520to%2520new%2520lines.%250A%2523%2520although%2520we%2520can%2520do%2520this%2520manually%2520too%252C%2520in%2520one%2520print%2520statement%250Aprint%28%27Hello%2520World%21%21%2520%255CnGet%2520ready%2520to%2520rock-N-roll%27%29%250A%2523%2520and%2520that%27s%2520how%2520we%2520do%2520it%2520%21%21"
    style="width: 612px; height: 238px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)
    github_gist("https://gist.github.com/bhanuchandrika/8279b541cad6dc9de9d22c2db12147e2", width=800)
    codearea()

def interact():
    st.subheader("**Interact with python**")
    st.markdown("""
    To do some work, we need something to begin with - right? For example, you need a bat and a ball to play cricket. Similarly, while coding we need some data or input from the user on which we will do some work.
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=seti&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523asking%2520user%2520for%2520a%2520text%2520%28name%29%250Ausername%2520%253D%2520input%28%27Please%2520enter%2520your%2520name%2520-%2520%27%29%250A%250A%2523lets%2520greet%2520the%2520user%2520now%250Aprint%2520%28%27Hello%2520%27%2520%252Busername%29%250A%250A%2523ask%2520the%2520user%27s%2520birth%2520year%250Ayear%2520%253D%2520input%28%27Please%2520enter%2520your%2520Birth%2520Year%2520-%2520%27%29%250A%250A%2523calculating%2520the%2520age%252C%2520here%2520we%2520have%2520to%2520change%2520the%2520type%2520for%2520year%2520from%2520string%2520to%2520integer%250Aage%2520%253D%25202021-%2520int%28year%29%250A%250A%2523now%2520we%2520will%2520print%2520the%2520results%250Aprint%28f%27Hey%2520%257Busername%257D%252C%2520You%2520are%2520%257Bage%257D%2520years%2520old%2520%253A%29%2520%27%29%250A%250A%2523using%2520%2522f%2522%2520before%2520writing%2520the%2520print%2520statement%2520saves%2520us%2520a%2520lot%2520of%2520time%2520and%2520effort%250A%2523just%2520need%2520to%2520keep%2520in%2520mind%2520that%2520we%2520are%2520keeping%2520the%2520variables%2520in%2520%257B%257D"
    style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)    
    github_gist("https://gist.github.com/bhanuchandrika/19633987195c8524a3a1d51f30c9032a", width=800)
    codearea()

def numbers():
    st.subheader("**Deal with numbers**")
    st.markdown("""
    So, in programming you can do lots of mathematical operations. But for that you need to have an idea of what are the various datatypes that are to be considered - or even not considered! This section will introduce with some of the possibilities and we'll cover the other complex stuff as we progress.
    <br><br>You've got it. Keep going! 🙂  
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=panda-syntax&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523%2520first%2520let%2520us%2520understand%2520the%2520datatypes.%250A%250A%2523%2520integer%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%252020%2520is%2520%257Btype%2820%29%257D%2522%29%2520%2523%2520%253Cclass%2520%27int%27%253E%250A%250A%2523%2520float%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%252020.02%2520is%2520%257Btype%2820.02%29%257D%2522%29%2520%2523%2520%253Cclass%2520%27float%27%253E%250A%250A%2523%2520string%2520datatype%250Aprint%28f%2522The%2520datatype%2520for%2520variable%2520%27abcd%2520efg%2520hijk%2520lmnop%27%2520is%2520%257Btype%28%27abcd%2520efg%2520hijk%2520lmnop%27%29%257D%2522%29%2520%2523%253Cclass%2520%27str%27%253E%250A%250A%2523get%2520the%2520binary%2520for%2520the%2520number%250Aprint%28bin%282020%29%29%2520%2523prints%2520the%2520binary%2520form%2520of%25202020%2520which%2520is%25200b11111100100%250A%2523get%2520number%28integer%29%2520from%2520binary%2520form%250Aprint%28int%28%270b11111100100%27%252C%25202%29%29%2520%2523%25202%2520for%2520printing%2520the%2520integer%2520form%2520by%2520base%2520as%25202%250A%250A%2523%2520----------------%2520that%2520would%2520be%2520enogh%2520for%2520now%2520to%2520understand%2520about%2520the%2520datatypes.%250A%250A%2523%2520Let%2520us%2520now%2520perform%2520some%2520arithmetic%2520operations%250A%250A%2523arithmetic%2520operations%2520without%2520variables%250Aprint%28f%2522Sum%2520of%25203%2520and%25205%2520is%2520%257B3%252B5%257D%2522%29%250Aprint%28f%2522difference%2520of%25203%2520and%25205%2520is%2520%257B3-5%257D%2522%29%250Aprint%28f%2522Product%2520of%25203%2520and%25205%2520is%2520%257B3*5%257D%2522%29%250Aprint%28f%2522Fraction%2520or%2520Division%2520of%25203%2520and%25205%2520is%2520%257B3%252F5%257D%2522%29%250Aprint%28f%2522exponent%2520of%25203%2520with%25205%2520is%2520%257B3**5%257D%2522%29%2520%2523exponent%250Aprint%28f%2522Modulus%2520of%25203%2520and%25205%2520is%2520%257B3%25255%257D%2522%29%2523mod%250A%250A%2523arithmetic%2520operations%2520with%2520variables%250A%250Aa%2520%253D%2520input%28%2522Enter%2520a%2520number.%2520It%2520will%2520be%2520stored%2520as%2520%27a%27%2520%253D%2520%2522%29%250Ab%2520%253D%2520input%28%2522Enter%2520another%2520number.%2520It%2520will%2520be%2520stored%2520as%2520%27b%27%2520%253D%2520%2522%29%250A%2523python%2520accepts%2520inputs%2520as%2520str.%2520So%2520whenever%2520we%2520need%2520to%2520perform%2520any%2520mathematical%2520operations%252C%2520we%2520need%2520to%2520change%2520the%2520datatypes%250A%250Aprint%28f%2522You%2520see%252C%2520I%2520am%2520writing%2520here%2520a%252Bb%2520but%2520the%2520output%2520will%2520not%2520be%2520the%2520sum.%2520%255CnInstead%252C%2520you%2520will%2520see%2520the%2520two%2520numbers%2520will%2520be%2520concatenated%21%2520%255CnHere%2520is%2520the%2520output%2520%253D%2520%257Ba%252Bb%257D%2522%29%250A%250Aa%2520%253D%2520float%28a%29%2520%2523keeping%2520in%2520float%2520is%2520safer%2520as%2520user%2520might%2520feed%2520data%2520with%2520decimals%250Ab%2520%253D%2520float%28b%29%2520%2523keeping%2520in%2520float%2520is%2520safer%2520as%2520user%2520might%2520feed%2520data%2520with%2520decimals%250A%250Aprint%28f%2522Sum%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%252Bb%257D%2522%29%250Aprint%28f%2522difference%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba-b%257D%2522%29%250Aprint%28f%2522Product%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba*b%257D%2522%29%250Aprint%28f%2522Fraction%2520or%2520Division%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%252Fb%257D%2522%29%250Aprint%28f%2522exponent%2520of%2520%257Ba%257D%2520with%2520%257Bb%257D%2520is%2520%257Ba**b%257D%2522%29%2520%2523exponent%250Aprint%28f%2522Modulus%2520of%2520%257Ba%257D%2520and%2520%257Bb%257D%2520is%2520%257Ba%2525b%257D%2522%29%2523mod"
    style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)
    github_gist("https://gist.github.com/ineelhere/13b6a1592d14ca05ef74b681803d65ed", width=800)
    codearea()

def math_func():
    st.subheader("**Math Functions**")
    st.markdown("""
    To make our lives easier, there are many in-built special functions that are very useful to do specific tasks.<br>
    Here we will see few of the in-built functions that can be used to perform mathematical operations.
    <iframe
    src="https://carbon.now.sh/embed?bg=rgba%280%2C0%2C0%2C0%29&t=panda-syntax&wt=none&l=python&ds=false&dsyoff=36px&dsblur=68px&wc=true&wa=true&pv=19px&ph=20px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=%2523%2520MATH%2520FUNCTIONS%2520IN%2520PYTHON%250A%2523%2520SOURCE%2520-%2520https%253A%252F%252Fdocs.python.org%252F3%252Flibrary%252Fmath.html%250A%2523--------------------------------------------------------------------------------------------------%250A%250A%2523%2520first%2520we%2520need%2520to%2520import%2520the%2520math%2520module%250A%2523%2520This%2520module%2520provides%2520access%2520to%2520the%2520mathematical%2520functions%2520defined%2520by%2520the%2520C%2520standard.%250A%2523%250A%2523%2520These%2520functions%2520cannot%2520be%2520used%2520with%2520complex%2520numbers%253B%2520use%2520the%2520functions%2520of%2520the%2520same%2520name%2520from%2520the%2520cmath%2520module%2520if%2520you%2520require%2520support%2520for%2520complex%2520numbers.%2520The%2520distinction%2520between%2520functions%2520which%2520support%2520complex%2520numbers%2520and%2520those%2520which%2520don%25E2%2580%2599t%2520is%2520made%2520since%2520most%2520users%2520do%2520not%2520want%2520to%2520learn%2520quite%2520as%2520much%2520mathematics%2520as%2520required%2520to%2520understand%2520complex%2520numbers.%2520Receiving%2520an%2520exception%2520instead%2520of%2520a%2520complex%2520result%2520allows%2520earlier%2520detection%2520of%2520the%2520unexpected%2520complex%2520number%2520used%2520as%2520a%2520parameter%252C%2520so%2520that%2520the%2520programmer%2520can%2520determine%2520how%2520and%2520why%2520it%2520was%2520generated%2520in%2520the%2520first%2520place.%250A%2523%250A%2523%2520The%2520following%2520functions%2520are%2520provided%2520by%2520this%2520module.%2520Except%2520when%2520explicitly%2520noted%2520otherwise%252C%2520all%2520return%2520values%2520are%2520floats.%250Aimport%2520%2520math%250A%250A%2523%2520--------------Number-theoretic%2520and%2520representation%2520functions--------------------------------------%250Along_string%2520%253D%2520%27%27%27%250Amath.ceil%28x%29%250AReturn%2520the%2520ceiling%2520of%2520x%252C%2520the%2520smallest%2520integer%2520greater%2520than%2520or%2520equal%2520to%2520x.%250AIf%2520x%2520is%2520not%2520a%2520float%252C%2520delegates%2520to%2520x.__ceil__%28%29%252C%2520which%2520should%2520return%2520an%2520Integral%2520value.%250A%27%27%27%250Aprint%28long_string%29%250A%250Aprint%28%2522%255Cn--------------------math.ceil%28x%29-------------------------------%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404%2520---%2520%257Bmath.ceil%28404%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.01%2520---%2520%257Bmath.ceil%28404.01%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.36%2520---%2520%257Bmath.ceil%28404.36%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.50%2520---%2520%257Bmath.ceil%28404.50%29%257D%2522%29%250Aprint%28f%2522math.ceil%28x%29%2520---%2520for%2520number%2520%253D%2520404.86%2520---%2520%257Bmath.ceil%28404.86%29%257D%2522%29%250Aprint%28%2522---------------------------------------------------------------%255Cn%2522%29%250A%250Along_string%2520%253D%2520%27%27%27%250Amath.comb%28n%252C%2520k%29%250AReturn%2520the%2520number%2520of%2520ways%2520to%2520choose%2520k%2520items%2520from%2520n%2520items%2520without%2520repetition%2520and%2520without%2520order.%250AEvaluates%2520to%2520n%21%2520%252F%2520%28k%21%2520*%2520%28n%2520"
    style="width: 810px; height: 469px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
    </iframe>
    """, unsafe_allow_html=True)
    github_gist("https://gist.github.com/ineelhere/c6b77aa48d3695c32712b18801adc43a", width=800)
    codearea()
