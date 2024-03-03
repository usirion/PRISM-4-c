# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:29:37 2024

@author: orlei.araujo
"""


from flask import Flask, render_template, request
import pandas as pd
Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('divs.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    prismn = None #prism neuro 
    prismnn = None #prism não-neuro 
    resultimc = None
    sd = None
    logit=None
    imcl = None #IMC < z score
    prob= None 
    # request.form looks for:
    # html tags with matching "name= "
        #operation = request.form['operation']
    weight = request.form['weight'] 
    stature = request.form['stature'] 
    sex = request.form['sex'] 
    stature = request.form['stature'] 
    age = request.form['age'] 
    pressaos = request.form['pressaos']  
    heart = request.form['heart']
    pressaos = request.form['pressaos']  
    temp = request.form['temp']
    glasgow = request.form['glasgow']  
    pupils = request.form['pupils']
    acidosis = request.form['acidosis']  
    alkalosis= request.form['alkalosis']
    pco2 = request.form['pco2']  
    tco2 = request.form['tco2']
    pao2 = request.form['pao2']  
    glucose = request.form['glucose']
    potassium = request.form['potassium']
    creat = request.form['creat']  
    urea = request.form['urea']
    leuc = request.form['leuc']
    plaq = request.form['plaq']  
    coag = request.form['coag']
    cir = request.form['cir']    
    irpa= request.form['irpa']
    sepsis= request.form['sepsis']
    leuclinf = request.form['leuclinf']
    
    try:
        age = float(age)
        input5=round(age,0)
        if sex=="F":
            file='girls.csv'        
            caf = pd.read_csv(file, sep = ';', decimal=',')
            loc_age=caf.loc[caf['mon'] == input5]
            sd= (loc_age.sd2neg)
            sd =sd
            sd=float(sd)
        else:
            file='boys.csv'        
            caf = pd.read_csv(file, sep = ';', decimal=',')
            loc_age=caf.loc[caf['mon'] == input5]
            sd= (loc_age.sd2neg)
            sd =sd
            sd =float(sd)
          
    except ValueError:
        return render_template(
            'divs.html',
                        #operation=operation,
            #sd ="No result",
            calculation_success=False,
            error="Something went wrong; please check if age is  <216 months, and if you completed all the items"
        ) 
    
    try:
        input3 = float(weight) #transforma strings em números
        input4 = float(stature)
        pressaos = float(pressaos)
        heart = float(heart)
        temp = float(temp)
        glasgow = float(glasgow)
        pupils = float(pupils)
        acidosis = float(acidosis)
        alkalosis = float(alkalosis)
        pco2 = float(pco2)
        tco2 = float(tco2)
        pao2 = float(pao2)
        glucose = float(glucose)
        potassium = float(potassium)
        creat = float(creat)
        urea = float(urea)
        leuc = float(leuc)
        plaq = float(plaq)
        coag = float(coag) 
        cir = int(cir)
        irpa= int(irpa)
        sepsis= int(sepsis)
        leuclinf = int(leuclinf)  
               
       # calcula IMC e checa se <z
        resultimc = input3/((input4/100)**2)
        if resultimc < sd:
            imcl = 1
        else:
            imcl = 0
            #calcula os prisms n e não-n
        prismn = glasgow + pupils
        prismnn = pressaos + heart + temp + acidosis + alkalosis + pco2 + tco2 +pao2 + glucose +potassium + creat + urea + leuc + plaq + coag
        logit= -4.110+(0.219*prismn)+(0.177*prismnn)+(1.264*leuclinf)+(1.841*sepsis)+(1.412*irpa)+(-1.16*cir)+(1.239*imcl)
        prob = (2.7182**logit/(1+2.7182**logit))*100
        return render_template(
                'divs.html',
                resultimc = round(resultimc,1), 
                sd=sd,
                sex=sex,
                imcl=imcl,
                prismn = prismn,
                prismnn=prismnn,
                logit=round(logit,2),
                prob= round(prob,1),
                calculation_success=True
            )
    except ZeroDivisionError:
        return render_template(
            'divs.html',
            
            result="Bad Input",
            calculation_success=False,
            error="You cannot divide by zero"
        )
        
    except ValueError:
        return render_template(
            'divs.html',
                        #operation=operation,
            #resultimc="No result",
            calculation_success=False,
            error="Cannot perform calculation. Please check if you completed all the items"
        )       

Flask_App.run()
