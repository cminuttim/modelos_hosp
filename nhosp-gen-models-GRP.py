#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Carlos Minutti Martinez <carlos.minutti@iimas.unam.mx>
@author: Miguel Félix Mata Rivera <mmatar@ipn.mx >

MODELO DE REGRESIÓN BINOMIAL NEGATIVA PARA PREDECIR EL NÚMERO DE HOSPITALIZACIONES

Resumen:

Mediante el análisis de datos de egresos hospitalarios, se ha desarrollado un 
sistema automatizado para la generación de modelos predictivos del número y la 
severidad de hospitalizaciones por diversas enfermedades y categorías, 
seleccionando los códigos CIE o grupos de códigos a modelar. Para tal fin, 
se han empleado técnicas estadísticas, tales como la regresión logística y la 
regresión binomial negativa.

No obstante, es importante destacar que los modelos generados no tienen como 
finalidad la predicción, ni están destinados a ser utilizados con ese propósito, 
sino que su objetivo es interpretar las variables que resultan relevantes a la 
hora de examinar la severidad y el número de hospitalizaciones. En este sentido, 
los modelos consideran el efecto de múltiples variables, tales como factores 
socioeconómicos, exposición a contaminantes ambientales, lugar de residencia, 
peso, edad, sexo, densidad de población, derechohabiencia, fecha de ingreso (con 
el fin de identificar patrones temporales) y se permite especificar el rango 
de años a utilizar. Por lo tanto, el interés radica en comprender cómo estas 
variables influyen en el modelo y 
la magnitud de su efecto.

Además, para mantener la interpretabilidad del modelo, se incluyen únicamente 
aquellas variables que contribuyen de manera significativa al mismo, a fin de 
que éste sea lo más parsimonioso posible y se reduzca el problema de 
multicolinealidad. Este procedimiento se lleva a cabo a través de un algoritmo 
ad-hoc que incluye penalizaciones en el proceso de selección de variables, y 
que toma en cuenta tanto la multicolinealidad como la paradoja de Simpson. En 
caso de que exista un efecto diferente al esperado (por ejemplo, de un análisis 
de correlación), se mantiene únicamente si su contribución al modelo resulta 
significativa.

El proceso de generación de los indicadores socioeconómicos y de contaminantes 
atmosféricos puede consultarse en los otros resultados de este proyecto.

Cabe destacar que, por motivos de privacidad, la base de datos original no se 
comparte. No obstante, se ha generado una versión con datos sintéticos que 
permite probar los algoritmos y adaptarlos para su uso en otros proyectos.


Licencia:    
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS


GitHub: https://github.com/cminuttim/
"""

from IPython import get_ipython;   
get_ipython().run_line_magic('reset','-sf')

import pickle
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import statsmodels.formula.api as smf




from tqdm.auto import tqdm

# Configuración del análisis a correr

class CFG:
    base_dir = './'      # Directorio base
    db = 'rnd_db.sqlite' # Base de datos a usar
    seed = 11            # Semilla para el componente aleatorio
    out = 'out/'         # Directorio de salida para las imágenes generadas
    save_plot = True     # ¿Se guardan las imágenes?
    train_prop = 0.85    # Proporción de registros para entrenamiento, (1-train_prop) para validación
    grp = 'PC'           # Tipo de análisis a realizar, PC: Principales causas de defunción, HE: Hospitalizaciones evitables, CM: Grupo especifico 
    max_grps = 2         # Número máximo de modelos a generar
    
    use_weight = False   # Usar mínimos cuadrados ponderados
    lang = 'EN'          # lang=EN o lang=ES para la salida de resultados
    use_defu = True      # ¿Usar solo CIE que tengan defunciones?

q_cond = 'ANIO<=2020'    # rango de años a usar para el análisis



# fijar semilla
np.random.seed(CFG.seed)



# CIE
# http://www.dgis.salud.gob.mx/contenidos/intercambio/diagnostico_gobmx.html

# CLUES
# http://www.dgis.salud.gob.mx/contenidos/intercambio/clues_gobmx.html

# PRINCAU
# LISTA MEXICANA PARA LA SELECCION DE LAS PRINCIPALES CAUSASDE MORTALIDAD
# http://dgis.salud.gob.mx/descargas/pdf/lista_mexicana.pdf



### Se cargan los catálogos de CIE Y CLUES ####
con = sqlite3.connect(CFG.base_dir + CFG.db)
cur = con.cursor()

clues = pd.read_sql_query('SELECT * FROM CATCLUES', con)
clues_export = clues.copy()
clues = clues.set_index(clues['CLUES'])

cie = pd.read_sql_query('SELECT * FROM CATCIE10', con)
cie_export = cie.copy()
cie.set_index('CAUSA', inplace=True)

# Catalogo de principales causas de defunción
df_princau = pd.read_sql_query('SELECT PRINCAU.descrip_padre, PRINCAU.principal FROM PRINCAU', con)


cie_caup = pd.read_sql_query('SELECT CATCIE10.CAUSA, PRINCAU.descrip_padre AS PCAU_PADRE_DESC \
	FROM CATCIE10 \
	INNER JOIN PRINCAU ON PRINCAU.principal = CATCIE10.prinmorta', con)
cie_caup.set_index('CAUSA', inplace=True)
cie = pd.concat([cie, cie_caup], axis=1)


# Catalogo de CIE consideradas cronicas
cie_c = pd.read_csv(CFG.base_dir + 'cie_cronicas.csv')

# Catalogos de hospitalizaciones evitables (Purdy y ACSCMex)
cie_hosp_e_Purdy = pd.read_csv(CFG.base_dir + 'cie-hosp_e_Purdy.csv')
cie_hosp_e_ACSCMex = pd.read_csv(CFG.base_dir + 'cie-hosp_e_ACSCMex.csv')
cie_hosp_e = pd.concat([cie_hosp_e_ACSCMex,cie_hosp_e_Purdy])
cie_hosp_e = cie_hosp_e[['CAUSA', 'CATEGORIA', 'NV0']]
cie_hosp_e.drop_duplicates(inplace=True)
cie_hosp_e.set_index('CAUSA', inplace=True)
cie_hosp_e.dropna(inplace=True)
hosp_e_cat = cie_hosp_e.CATEGORIA.unique()

cie_hosp_gdesc = pd.read_csv(CFG.base_dir + 'cie-hosp_gdesc.csv')
cie_hosp_gdesc.set_index('Code', inplace=True)


con.close()



# Traducción de variables de fecha
day_es = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
day_en = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_en_es = {day_en[i]: day_es[i] for i in range(len(day_en))}

month_es = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
month_en = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_en_es = {month_en[i]: month_es[i] for i in range(len(month_en))}

# Traducción de algunos grupos de enfermedades
grp_en = {}
grp_en['DC'] = '[E10–E14] Diabetes mellitus'
grp_en['E112'] = '[E112] Type 2 diabetes mellitus with kidney complications'
grp_en['E117'] = '[E117] Type 2 diabetes mellitus with multiple complications'
grp_en['E145'] = '[E145] Unspecified diabetes mellitus: with peripheral circulatory complication'
grp_en['E118'] = '[E118] Type 2 diabetes mellitus with unspecified complications'


grp_en['E10-E149'] = 'Diabetes mellitus'
grp_en['A15-Z999'] = 'Other'
grp_en['J09X-U049'] = 'Influenza and Pneumonia'
grp_en['K70-K769'] = 'Liver diseases'
grp_en['I00X-I519'] = 'Heart diseases'
grp_en['U072-U072'] = 'COVID-19, virus unidentified'
grp_en['I60-I698'] = 'Cerebrovascular Diseases'
grp_en['A33X-P969'] = 'Certain conditions originating in the perinatal period'
grp_en['U071-U071'] = 'COVID-19, virus identified'
grp_en['N17-N19X'] = 'Renal insufficiency'



#########################################
## INEGI VARS 
#########################################
#
# Se cargan los datos del Censo de Población y Vivienda 2020 (INEGI), así como 
# las variables y ponderaciones para construir los indicadores socioeconómicos por localidad
# 
# Valores (999,9999)  indican que tienen municipio o localidad desconocida 

inegi_vars = pd.read_csv(CFG.base_dir + './variables.csv')
inegi_loc = pd.read_csv(CFG.base_dir + './inegi_loc.csv', dtype={'ENTIDAD':'str','MUN':'str','LOC':'str'})
area_ageb = pd.read_csv(CFG.base_dir + './ageb-area.csv', dtype={'CVE_ENT':'str','CVE_MUN':'str','CVE_LOC':'str','CVE_AGEB':'str'})
inegi_fa_loads = pd.read_csv(CFG.base_dir + './inegi_fa_loads.csv')
scale_inegi_fa = pd.read_csv(CFG.base_dir + './scale_inegi_fa.csv').transpose()
inegi_fa_loads.set_index('Var', inplace=True)
scale_inegi_fa.rename(columns = {0:'min', 1:'max'}, inplace = True)

area_ageb['loc_id'] = area_ageb['CVE_ENT'] + area_ageb['CVE_MUN'] + area_ageb['CVE_LOC']
area_loc = area_ageb.groupby(['loc_id'])['Area'].sum().reset_index()
area_loc.set_index('loc_id', inplace=True)


id_inegi = (inegi_loc['ENTIDAD']+inegi_loc['MUN']+inegi_loc['LOC'])

inegi_loc.set_index(id_inegi, inplace=True)


idx = inegi_loc.index[inegi_loc.index.isin(area_ageb['loc_id'])].to_numpy()

inegi_loc = inegi_loc.assign(AREA=area_loc.Area.min())  #usar el area minima como estimado para aquellos que no aparecen
inegi_loc.loc[idx, 'AREA'] = area_loc.loc[idx, 'Area']


idx_scalable = inegi_loc.columns.isin(inegi_vars.Var[inegi_vars.No_Esc==0])
idx_scale = inegi_loc.columns[idx_scalable]
idx_pob = inegi_loc.columns[[i[0]=='P' for i in inegi_loc.columns]*idx_scalable]
idx_viv = inegi_loc.columns[[i[0]=='V' for i in inegi_loc.columns]*idx_scalable]

inegi_loc_s = inegi_loc.copy()


inegi_loc_s[idx_pob] = inegi_loc[idx_pob].div(inegi_loc['POBTOT'], axis=0)
inegi_loc_s[idx_viv] = inegi_loc[idx_viv].div(inegi_loc['VIVTOT'], axis=0)

inegi_loc_s['POBTOT'] = inegi_loc['POBTOT']/inegi_loc['POBTOT'].sum()
inegi_loc_s['VIVTOT'] = inegi_loc['VIVTOT']/inegi_loc['VIVTOT'].sum()

inegi_loc_s = inegi_loc_s.assign(POB_AREA=inegi_loc['POBTOT']/inegi_loc['AREA'])

id_p = inegi_loc_s.columns.get_loc('POBTOT')


nom_ent = inegi_loc['NOM_LOC']
nom_ent.loc['099990001'] = 'Municipio desconocido'
nom_ent.loc['159990001'] = 'Municipio desconocido'
inegi_loc = inegi_loc_s
inegi_loc.iloc[:,id_p:]

main_inegi_vars = ['POBTOT', 'POB_AREA', 'P_0A2', 'P_18A24', 'P_60YMAS', 'POB0_14', 'POB15_64', 'POB65_MAS', 'REL_H_M', 'PROM_HNV', 'GRAPROES', 'PROM_OCUP', 'P3HLINHE_M', 'P5_HLI_NHE', 'PDER_IMSS', 'PDER_ISTE', 'PDER_ISTEE', 'PAFIL_PDOM', 'PDER_SEGP', 'PDER_IMSSB', 'PAFIL_IPRIV', 'VIVPAR_UT', 'VPH_PISOTI', 'VPH_1CUART', 'VPH_AGUAFV', 'VPH_LETR', 'VPH_NODREN', 'VPH_SNBIEN', 'VPH_SINRTV', 'VPH_SINTIC']
inegi_loc = inegi_loc[main_inegi_vars]
id_inegi_fa = inegi_loc.columns.get_loc('REL_H_M')

id_p = 0

inegi_vars.set_index(inegi_vars.Var, inplace=True)

#--------------------------






#########################################
## CONTAMINANTES  
#########################################
#
# Se cargan las concentraciones de contaminantes y las ponderaciones
# para construir los indicadores (factores) de contaminantes por localidad.
# Estos factores tienen la finalidad de solventar el problema de contaminantes 
# correlacionados espacialmente (multicolinealidad), al agrupar en factores de
# aquellos que tienden a estar presentes de manera simultanea.

cont_loc = pd.read_csv(CFG.base_dir + './cont_loc_mean.csv', dtype={'ENTIDAD':'str','MUN':'str','LOC':'str'})
id_cont = (cont_loc['ENTIDAD']+cont_loc['MUN']+cont_loc['LOC'])

scale_cont_fa = pd.read_csv(CFG.base_dir + './scale_cont_fa.csv').transpose()
scale_cont_fa.rename(columns = {0:'min', 1:'max'}, inplace = True)



cont_loc.set_index(id_cont, inplace=True)
idx = cont_loc.index.isin(inegi_loc.index)
cont_loc = cont_loc[idx]
cont_loc.drop(['ENTIDAD', 'MUN', 'LOC'], axis=1, inplace=True)










#########################################
## MAIN  
#########################################


# carga de datos
db_year = range(15,21)
year = range(2015,2021)

        
db_file = CFG.base_dir + CFG.db
    
con = sqlite3.connect(db_file)
cur = con.cursor()
        
df_afec = pd.read_sql_query(f'SELECT * FROM AFECCIONES WHERE {q_cond}', con)    
df_egre = pd.read_sql_query(f'SELECT * FROM EGRESO WHERE ({q_cond} AND (ENTIDAD="09"))', con)    
df_defu = pd.read_sql_query(f'SELECT DEFUNC.*, EGRESO.DIAGNOSTICO, EGRESO.AFECCION, EGRESO.DIAS, EGRESO.EDAD, EGRESO.SEXO, EGRESO.PESO, EGRESO.TALLA, EGRESO.PROCED, EGRESO.DERHAB, EGRESO.VEZ, \
                            EGRESO.ENTIDAD, EGRESO.MUNIC, EGRESO.LOC, EGRESO.INGRESO \
                            FROM DEFUNC \
                            INNER JOIN EGRESO on EGRESO.FOLIO = DEFUNC.FOLIO AND EGRESO.CLUES = DEFUNC.CLUES AND EGRESO.EGRESO = DEFUNC.EGRESO \
                            WHERE (DEFUNC.{q_cond} AND (EGRESO.ENTIDAD="09"))', con)    


 
con.close()



def shuffle_data(df):
        
    n, m = df.shape
    
    df = df.reset_index(drop=True)
    for i in range(m):
        df.iloc[:,i] = df.iloc[:,i].sample(frac=1).reset_index(drop=True)
        
    return df
    




# remover espacio al final (array(['0 ', '8 ', 'G ', '9 ', '6 ', '2 '], dtype=object))
df_egre.DERHAB = df_egre.DERHAB.str[:-1] 
df_defu.DERHAB = df_defu.DERHAB.str[:-1]



# get summary statistics 
num_cols_afec = df_afec._get_numeric_data().columns
df_afec_num_desc = df_afec[num_cols_afec].describe(percentiles=[.05, .25, .5, .75, .95]).transpose()
df_afec_cat_desc = df_afec.iloc[:,~df_afec.columns.isin(num_cols_afec)].describe().transpose()
df_afec_cat_desc['perc'] = (df_afec_cat_desc['freq']/df_afec_cat_desc['count']*100).astype('float')

num_cols_egre = df_egre._get_numeric_data().columns
df_egre_num_desc = df_egre[num_cols_egre].describe(percentiles=[.05, .25, .5, .75, .95]).transpose()
df_egre_cat_desc = df_egre.iloc[:,~df_egre.columns.isin(num_cols_egre)].describe().transpose()
df_egre_cat_desc['perc'] = (df_egre_cat_desc['freq']/df_egre_cat_desc['count']*100).astype('float')

num_cols_defu = df_defu._get_numeric_data().columns
df_defu_num_desc = df_defu[num_cols_defu].describe(percentiles=[.05, .25, .5, .75, .95]).transpose()
df_defu_cat_desc = df_defu.iloc[:,~df_defu.columns.isin(num_cols_defu)].describe().transpose()
df_defu_cat_desc['perc'] = (df_defu_cat_desc['freq']/df_defu_cat_desc['count']*100).astype('float')




# Eliminar outliers
df_egre.loc[df_egre.EDAD>120,'EDAD'] = np.nan
df_egre.loc[df_egre.PESO>250,'PESO'] = np.nan
df_egre.loc[df_egre.TALLA>250,'TALLA'] = np.nan


df_defu.loc[df_defu.EDAD>120,'EDAD'] = np.nan
df_defu.loc[df_defu.PESO>250,'PESO'] = np.nan
df_defu.loc[df_defu.TALLA>250,'TALLA'] = np.nan




# tablas de conteo para los diagnósticos
n_egre_cie = df_egre.groupby('DIAGNOSTICO')['DIAGNOSTICO'].count().sort_values(ascending=False)
n_defu_cie_bas = df_defu[['CAUSA']].groupby('CAUSA')['CAUSA'].count().sort_values(ascending=False)
n_defu_cie_bas = pd.concat([n_defu_cie_bas, cie.loc[n_defu_cie_bas.index,'Nombre']], axis=1)
n_defu_cie_bas.rename(columns = {'CAUSA':'count'}, inplace = True)


# Por edad
edad_cie = df_defu.pivot_table(['EDAD'],
               ['CAUSA'],
                aggfunc=lambda x: [np.percentile(x, [25, 50, 75])],
    )
edad_cie = pd.DataFrame(np.asmatrix(list(map(lambda a:a[0],edad_cie.EDAD))), 
             index=edad_cie.index, 
             columns=['edad_Q1', 'edad_Q2', 'edad_Q3',])
edad_cie = pd.concat([edad_cie, cie.loc[edad_cie.index,'Nombre']], axis=1)
edad_cie_def = edad_cie.copy()

# Por sexo
sexo_cie = df_defu.pivot_table(['SEXO'],
               ['CAUSA'],
                aggfunc=lambda x: np.round([np.mean(x=='F'), np.mean(x=='M')],3),
    )
sexo_cie = pd.DataFrame(np.asmatrix(list(sexo_cie.SEXO)), 
                 index=sexo_cie.index, 
                 columns=['SEXO_F', 'SEXO_M'])

sexo_cie_def = sexo_cie.copy()

idx_sel = edad_cie_def.index.isin(n_defu_cie_bas.index) # should be 100%
cie_def = edad_cie_def.loc[idx_sel,]
cie_def.loc[:,'count'] = n_defu_cie_bas.loc[cie_def.index,'count']

cie_def[['SEXO_F', 'SEXO_M']] = sexo_cie_def.loc[cie_def.index,['SEXO_F', 'SEXO_M']]

# Por edad y sexo
cie_def = cie_def[['edad_Q1', 'edad_Q2', 'edad_Q3', 'SEXO_F', 'SEXO_M', 'Nombre', 'count']].sort_values(by=['count'], ascending=False)
cie_def_sel = cie_def.iloc[:50,]



# Se transforma la fecha a variable de tiempo
df_egre.EGRESO = pd.to_datetime(df_egre.EGRESO)
df_defu.EGRESO = pd.to_datetime(df_defu.EGRESO)
df_afec.EGRESO = pd.to_datetime(df_afec.EGRESO)




# Se construye un identificador único de registro
df_egre['ID'] = df_egre['FOLIO'].map(str) + '_' + df_egre['CLUES'].map(str) + '_' + df_egre['EGRESO'].dt.strftime('%Y-%m-%d')
df_defu['ID'] = df_defu['FOLIO'].map(str) + '_' + df_defu['CLUES'].map(str) + '_' + df_defu['EGRESO'].dt.strftime('%Y-%m-%d')
df_afec['ID'] = df_afec['FOLIO'].map(str) + '_' + df_afec['CLUES'].map(str) + '_' + df_afec['EGRESO'].dt.strftime('%Y-%m-%d')

df_egre.INGRESO = pd.to_datetime(df_egre.INGRESO)
df_defu.INGRESO = pd.to_datetime(df_defu.INGRESO)

# Fecha como un valor numerico del mes-año
df_egre['FECHA'] = df_egre.INGRESO.dt.month + 12*(df_egre.INGRESO.dt.year-2015)
df_defu['FECHA'] = df_defu.INGRESO.dt.month + 12*(df_defu.INGRESO.dt.year-2015)

df_egre['MES'] = df_egre.INGRESO.dt.month_name()
df_defu['MES'] = df_defu.INGRESO.dt.month_name()


df_egre['QN'] = df_egre.INGRESO.dt.quarter
df_defu['QN'] = df_defu.INGRESO.dt.quarter

df_egre['ANIO'] = df_egre.INGRESO.dt.year
df_defu['ANIO'] = df_defu.INGRESO.dt.year

df_egre['DIA_SEMANA'] = df_egre.INGRESO.dt.day_name()
df_defu['DIA_SEMANA'] = df_defu.INGRESO.dt.day_name()


# Función para escalar los datos a 0-1
def min_max_scaler(X, xmin=None, xmax=None):
    
    if type(xmin)==type(None):
        xmin = X.min()
    else:
        xmin = xmin[X.columns.values]
    if type(xmax)==type(None):
        xmax = X.max()
    else:
        xmax = xmax[X.columns.values]
    
    X_tmp = X.copy()
        
    # constant values to 0
    idx = xmin.index[xmin==xmax]
    idx = idx[idx.isin(X_tmp.columns)]
    if idx.shape[0]>0:
        X_tmp[idx] = 0
    
    idx = xmin.index[(xmin<xmax) * ((xmin!=0) + (xmax!=1))]
    idx = idx[idx.isin(X_tmp.columns)] # only available columns
    
    X_tmp[idx] = (X_tmp[idx]-xmin[idx])/(xmax[idx]-xmin[idx])

    return (X_tmp, xmin, xmax)

# Función para limitar el rango de una variable
def x_set_lim(X, ll, ul):

    X_l = X.copy()
    
    X_l[X_l<ll] = ll
    X_l[X_l>ul] = ul
    
    return X_l

#------------------------------------------------------------------
# Modelos
#------------------------------------------------------------------

df_egre_not_defu =  df_egre.loc[~df_egre['ID'].isin(df_defu['ID']),]


# lista de códigos CIE para las defunciones en la base de datos
causas_defu = pd.Series(df_defu.CAUSA.unique())
cie_xcat = causas_defu[~(causas_defu.isin(df_egre_not_defu.AFECCION) + causas_defu.isin(df_egre_not_defu.DIAGNOSTICO))]
cie_xcat = cie_xcat[cie_xcat.isin(cie_def.index)].values
cie_def.drop(cie_xcat, axis=0, inplace=True)

# percentage of death causes in the chronic db
idx_c = cie_def.index.isin(cie_c['cie'])
idx_c.sum()/idx_c.shape[0]

cie_def_c = cie_def.iloc[idx_c,]

np.log10(cie_def['count']).hist()
n_egre_in_def_cie = n_egre_cie[n_egre_cie.index.isin(cie_def.index)]

# al menos 20 defunciones con esa causa (por posibles CIE que se pusieron como causa de del pero no lo son)
n_egre_in_def_cie = n_egre_in_def_cie[cie_def['count'][n_egre_in_def_cie.index]>20] 



# Inicialización de variables para los modelos a generar
cum_val_sc_reg = 0
cum_val_sc_reg2 = 0
cum_val_sc_reg3 = 0
cum_val_sc_tree = 0
cum_val_sc_gbm = 0
cum_val_sc_hgbm = 0
cum_val_mse = 0
cum_val_mse2 = 0
cum_val_sc_mix = 0

models_dict = {}
models = []
model_vars = pd.Series(dtype=object)



# Calcular la variable dependiente Y
# Usa días de hospitalización como variable de severidad y afecciones
# relaciona menos días en defunciones con más severidad
# menos días en egresos (no defunc) con menos severidad


# avoid warnings using assign
df_egre_not_defu = df_egre_not_defu.assign(Y=0.0)
df_defu = df_defu.assign(Y=1.0)

# Create Y as 0-1
max_d = 150
fx = np.log(max_d+1)-np.log(df_defu.DIAS+1)
fx[fx<0] = 0
df_defu['Y'] = 1/(1+np.exp(-1.0*fx))

fx = np.log(df_egre_not_defu.DIAS+1)-np.log(max_d+1)
fx[fx>0] = 0
df_egre_not_defu['Y'] = 1/(1+np.exp(-1.0*fx))


# Variable para almacenar cuantas veces fue relevante una variable socioeconómica en los modelos
inegi_v_model = pd.DataFrame(['F_ECONOM', 'F_SOCIAL'], columns=['var'])
inegi_v_model = inegi_v_model.assign(count=0)
inegi_v_model.set_index('var', inplace=True)


# Variable para almacenar cuantas veces fue relevante una variable de contaminantes en los modelos
cont_v_model = pd.DataFrame(['PM_CO', 'NO2_NOx', 'SO2_NO_O3'], columns=['var'])
cont_v_model = cont_v_model.assign(count=0)
cont_v_model.set_index('var', inplace=True)



# lista de localidades
loc_id = pd.DataFrame(df_defu['ENTIDAD'] + df_defu['MUNIC'] + df_defu['LOC'], columns=['loc'])

# registros por localidad
loc_n = loc_id.groupby(['loc'])['loc'].count().sort_values(ascending = False)
prop_ine = []

# Inicialización de variables
cie_id = []
cie_name = []
cie_reg_err = []
cie_reg_cor = []
cie_inegi_vars = []
cie_cont_vars = []
cie_emun_vars = []
cie_negv = []
cie_time = []
cie_sexo = []
cie_only_pobtot = []
cie_cronic = []
cie_pred_outliers = []
cie_n_cases = []




# Determinar la lista de códigos CIE o de grupos a utilizar según la configuración
cie_grp = {}
cie_grp_desc = {}
grp_n_regs = {}

if CFG.grp == 'HE':
    for i,grp in enumerate(hosp_e_cat):
        cie_grp[grp] = cie_hosp_e.index[cie_hosp_e.CATEGORIA == grp].tolist()
        cie_grp_desc[grp] = cie_hosp_gdesc.ES_Desc[grp]
        
        cie_tmp = pd.Series(cie_grp[grp])
        cie_tmp = cie_tmp[cie_tmp.str.len()==3]
        
        for j,x in enumerate(cie_tmp):
            cie_grp[grp] += cie.index[cie.index.str.match(x+'.')].tolist()
    
        grp_n_regs[grp] = ((df_egre.AFECCION.isin(cie_grp[grp])) + (df_egre.DIAGNOSTICO.isin(cie_grp[grp]))).sum()
        

if CFG.grp == 'PC':
    pcau_padre = cie.PCAU_PADRE_DESC.dropna().unique()
    for i,grp in enumerate(pcau_padre):
        cie_lst = cie.index[cie.PCAU_PADRE_DESC == grp].tolist()
        grp_id = cie_lst[0]+'-'+cie_lst[-1]
        cie_grp[grp_id] = cie_lst
        cie_grp_desc[grp_id] = grp
        grp_n_regs[grp_id] = ((df_egre.AFECCION.isin(cie_lst)) + (df_egre.DIAGNOSTICO.isin(cie_lst))).sum()
        if CFG.use_defu:
            grp_n_regs[grp_id] = df_defu.CAUSA.isin(cie_lst).sum()
    

if CFG.grp == 'CM':
    cie_lst = cie.index[cie.PCAU_PADRE_DESC == 'Diabetes mellitus'].tolist()
    idx = n_egre_in_def_cie.index.isin(cie_lst)
    idx_cie = n_egre_in_def_cie.index[idx]
    for i,grp in enumerate(idx_cie):
        cie_grp[grp] = [grp]
        cie_grp_desc[grp] = cie.Nombre[grp]
        grp_n_regs[grp] = ((df_egre.AFECCION.isin([grp])) + (df_egre.DIAGNOSTICO.isin([grp]))).sum()


df_grp = pd.DataFrame(data={'grp':cie_grp.keys(), 'cie':cie_grp.values(), 'desc':cie_grp_desc.values(), 'n_regs':grp_n_regs.values()})    
df_grp = df_grp.sort_values(by=['n_regs'], ascending=False).reset_index(drop=True)
df_grp.set_index('grp', inplace=True)
print(df_grp)

df_princau = df_princau[df_princau.descrip_padre.isin(df_grp.desc.values[1:20])]



    

def rep_outlier(X, d=0.001, max_p=1.4):
    
    X_up = X.quantile(1-d)

    idx_up = X.max().div(X_up)>max_p
  
    X_c = X.copy()

    for i in X.columns[idx_up]:
        X_c.loc[X_c[i]>X_up[i],i] = X_up[i]
        
    return X_c    


    
gbm_score_dict = {}
#------------------------------------------------------------------
# cie list
#------------------------------------------------------------------

for cie_iter, grp in enumerate(tqdm(df_grp.index[:CFG.max_grps], desc='Modelo')):

    # Codigos CIE y descripcion para el grupo actual
    cie_x = df_grp.cie[grp]
    cie_x_desc  = df_grp.desc[grp]
    
    
    # Determinar la lista de registros que cumplen con el grupo a estudiar
    df_egre_cie = df_egre_not_defu.loc[(df_egre_not_defu.AFECCION.isin(cie_x)) + (df_egre_not_defu.DIAGNOSTICO.isin(cie_x)), :]
    df_defu_cie = df_defu.loc[(df_defu.AFECCION.isin(cie_x)) + (df_defu.DIAGNOSTICO.isin(cie_x)) + (df_defu.CAUSA.isin(cie_x)), :]
    id_lst = pd.concat([df_egre_cie.ID, df_defu_cie.ID])
    
    tmp = []
    
    
    # Se reinicia semilla para cada grupo a estudiar
    np.random.seed(CFG.seed)
    
    
    
    
    
    
    #------------------------------------------------------------------
    # Data Frame
    #------------------------------------------------------------------    

    vars_n = ['Y', 'EDAD', 'SEXO', 'PESO', 'PROCED', 'VEZ', 'ENTIDAD', 'MUNIC', 'LOC', 'FECHA', 'MES', 'ANIO']
    tmp = pd.concat([df_egre_cie[vars_n], df_defu_cie[vars_n]], axis=0).set_index(id_lst)
        
    X_df = tmp
    
    X_df.isnull().sum()
    X_df['EDAD'].fillna(X_df['EDAD'].median(), inplace = True)
    X_df['PESO'].fillna(X_df['PESO'].median(), inplace = True)
    
    # La variable TALLA no es confiable, por lo que no se usa
    #X_df['TALLA'].fillna(X_df['TALLA'].median(), inplace = True)




    #------------- VARIABLES SOCIOECONOMICAS  ------------------
    loc_id = pd.DataFrame(X_df['ENTIDAD'] + X_df['MUNIC'] + X_df['LOC'], columns=['loc'])
    

    idx_avail_loc = loc_id['loc'].isin(inegi_loc.index)
    prop_ine.append(idx_avail_loc.mean())
    
    X_df = X_df[idx_avail_loc]
    loc_id = loc_id[idx_avail_loc]
    
    X_inegi = inegi_loc.loc[loc_id['loc'],:]
    X_inegi = X_inegi.iloc[:,id_p:]
    X_inegi.set_index(X_df.index, inplace=True)


    X_inegi_s, X_inegi_min, X_inegi_max = min_max_scaler(X_inegi.iloc[:,id_inegi_fa:], scale_inegi_fa['min'], scale_inegi_fa['max'])
    X_inegi_s = x_set_lim(X_inegi_s, -1, 10) # avoid outliers
    X_inegi_fa = X_inegi_s.dot(inegi_fa_loads.loc[X_inegi_s.columns,:])
    X_inegi_fa.rename(columns = {'F1':'F_ECONOM', 'F2':'F_SOCIAL'}, inplace = True)    
    X_df = pd.concat([X_df, X_inegi_fa, X_inegi[['POBTOT', 'POB0_14', 'POB15_64', 'POB65_MAS', 'REL_H_M', 'POB_AREA']]], axis=1)

    X_df['E_MUN'] = X_df['ENTIDAD'] + X_df['MUNIC']
    X_df.drop(['MUNIC', 'LOC'], axis=1, inplace=True)
    #-------------------

    X_df['MES_ANIO_LOC'] =  X_df['MES'] + '_' + X_df['ANIO'].astype(str) + '_' + loc_id['loc']



    #------------- VARIABLES DE CONTAMINANTES  ------------------
    idx_avail_loc = loc_id['loc'].isin(cont_loc.index)
    
    # Mantener unicamente localidades conocidas    
    X_cont = cont_loc.loc[loc_id['loc'],:]
    X_cont.set_index(X_df.index, inplace=True)
    X_cont_s, X_cont_min, X_cont_max = min_max_scaler(X_cont, scale_cont_fa['min'], scale_cont_fa['max'])
    
    X_cont_s['PM_CO'] = 0.35*X_cont_s['pm10_mean'] + 0.39*X_cont_s['pm25_mean'] + 0.26*X_cont_s['co_mean']
    X_cont_s['NO2_NOx'] = 0.54*X_cont_s['no2_mean'] + 0.46*X_cont_s['nox_mean'] 
    X_cont_s['SO2_NO_O3'] = 0.35*X_cont_s['so2_mean'] + 0.33*X_cont_s['no_mean'] + 0.32*X_cont_s['o3_mean']  
    
    X_cont_s.drop(cont_loc.columns, axis=1, inplace=True)
    
    X_df = pd.concat([X_df, X_cont_s], axis=1)
    #-------------------



    
    # Predictoras
    X = X_df.copy()
    
    # Incluir otras variables categóricas a través de dummies
    X = pd.concat((X, pd.get_dummies(X['SEXO'], prefix='SEXO', drop_first=True)), axis=1)
    X = pd.concat((X, pd.get_dummies(X['E_MUN'], prefix='E_MUN', drop_first=False)), axis=1)
    X = pd.concat((X, pd.get_dummies(X['ENTIDAD'], prefix='ENTIDAD', drop_first=True)), axis=1)
    X = pd.concat((X, pd.get_dummies(X['MES'], prefix='MES', drop_first=False)), axis=1)

    y = X['Y']
    X.drop(['SEXO', 'PROCED', 'VEZ'], axis=1, inplace=True)
    X.drop(['ENTIDAD', 'E_MUN', 'MES', 'ANIO'], axis=1, inplace=True)
    X_df.drop(['ENTIDAD'], axis=1, inplace=True)
    bool_cols = X.columns[X.dtypes=='bool']
    X[bool_cols] = X[bool_cols].astype('int')
    X.describe().transpose()
    X.dtypes.unique()
    X.reset_index(drop=True, inplace=True)
    y.reset_index(drop=True, inplace=True)
    

    
    # Eliminar algunos outliers encontrados y errores de captura
    if any((X.EDAD==0) * (X.PESO>10)):
        X.loc[(X.EDAD==0) * (X.PESO>10),'PESO'] = X.PESO[X.EDAD==0].median()
    if np.quantile(X.EDAD, 0.995)==0 and X.EDAD.max()>0: # Para cuando la mayoria son edad 0
        X.loc[X.EDAD>0,'EDAD'] = 0
        
    data_err1 = (X.EDAD>10) * (X.PESO<10)
    data_err2 = (X.PESO==9.999) + (X.PESO==9.099) + (X.PESO==0.999)
    if any(data_err1):             # Pesos sin sentido por culpa de variaviones de 999
        X.loc[data_err1,'PESO'] = X.PESO[~data_err1].median()
    if any(data_err2):             # variaciones de 999, como 9, 9.99, 0.99 u otros para pesos no especificados
        X.loc[data_err2,'PESO'] = X.PESO[~data_err2].median()
        
        
    # Incluir contaminantes, socioeconómicas
    main_var = pd.Series(['EDAD', 'PESO', 'SEXO_M', 'F_ECONOM', 'F_SOCIAL', 'PM_CO', 'NO2_NOx', 'SO2_NO_O3'])
    main_var = main_var[main_var.isin(X.columns)] # Algunas como SEXO_M podrian no existir por ser todas mujeres
    X_main = X[main_var]
    X.drop(['EDAD', 'PESO', 'SEXO_M'], axis=1, inplace=True, errors='ignore')



    # -------------------------------------------------
    # ----- X y Y por mes, se usa media o mediana, y se puede eliminar o no valores 0
    # ----- Y es el número ce casos por mes y localidad
    # -------------------------------------------------
    y = X.groupby('MES_ANIO_LOC')['MES_ANIO_LOC'].count()
    X = X.groupby('MES_ANIO_LOC').mean()
    X['Y'] = y 
    

    
    # Reescalar los predictores
    X_s, xmin, xmax = min_max_scaler(X)
    X_s_desc = X_s.describe().transpose()
    X_s['Y'] = X['Y']
    
    

    

    
    y_corr = X_s.corr(method='spearman')
    corr_y = y_corr[['Y']][1:]
    best_vars = y_corr['Y'].abs().sort_values(ascending=False).index
    
            
    msk = np.random.rand(len(X_s)) < CFG.train_prop
    train_desc = X_s[msk].describe().transpose()
    test_desc = X_s[~msk].describe().transpose()
    train_std = X_s.columns[train_desc['std']>0]

    X_s = X_s[train_std]
    X = X[train_std]    
    
    # train and test set
    train = X_s[msk]
    test = X_s[~msk]


    
    

    #------------------------------------------------------------------
    # Regresion Binomial Negativa (Variable selection)
    #------------------------------------------------------------------  
    #
    # Regresion Binomial Negativa con selección de variables. Sólo se mantienen las 
    # variables que contribuyen significativamente al modelo para que éste sea 
    # lo más parsimonioso posible y reducir el problema de la multicolinealidad. 
    
    # Se incluyen penalizaciones en el proceso de selección de variables teniendo 
    # en cuenta el problema de la multicolinealidad y la paradoja de Simpson, como 
    # no permitir que el signo de la variable sea diferente del signo de 
    # correlación a menos que la contribución al modelo sea significativa 
    # al hacerlo. 
    
    # Todas estas consideraciones mantienen la interpretabilidad del modelo.
    
    # El algoritmo prueba eliminando variables con poca significación estadística 
    # y mantiene los modelos con mejor AIC considerando las penalizaciones 
    # mencionadas. Cambien prueba incluyendo variables de forma iterativa, 
    # incluyendo aquellas con mejor correlación con la variable dependiente.
    
    

    # Se inicia solo con las variables que tienen una correlación mínima
    # El valor umbral es pequeño ya que la relación puede ser no lineal
    best_vars_cor = corr_y.Y.abs()[(corr_y.Y.abs()>0.01)].sort_values(ascending=False).index
    best_vars_cor = best_vars_cor[best_vars_cor.isin(train.columns)]

    sif_vars = pd.Series(best_vars_cor)
    sif_vars0 = sif_vars.copy()
    init_n_vars = 10
    sif_vars = sif_vars[:init_n_vars]


    sif_vars = sif_vars[sif_vars.isin(train.columns)]


    p_vals = pd.Series([1,1,1,0])
    p_var = p_vals
    n_it = 0
    n_it_ch = 0
    n_forw = 0

    max_n_it_ch = 2*len(best_vars_cor)
    max_p_val = 0.15
    max_p_val_final = 0.05
    delta_p = 0.001
    keep_going = False

    removed_vars = np.array([])
    prev_ic = np.inf
    best_ic = np.inf
    
    pob_vars = ['POBTOT', 'POB0_14', 'POB15_64', 'POB65_MAS']
    neg_vars = np.concatenate([X_cont_s.columns, X_inegi_fa.columns, pob_vars])
    neg_v = np.inf
    n_nvars = neg_vars.shape[0]
    l_neg = 0.2   # Penalizacion que busca principalmente variables que aumentan el riesgo
    l_cor = 0.025 # Penalizacion para variables que cambian el signo en su correlacion
    
    
    
    # proceso iterativo de selección de variables
    while (n_it-n_it_ch)<max_n_it_ch:
        
        sif_vars_f = '+'.join(sif_vars)        
            
        glm = smf.glm(
            'Y~'+sif_vars_f,
            data=train,
            family=sm.families.NegativeBinomial())
        
        cie_model = glm.fit()
        

        p_vals = cie_model.pvalues[1:]

        if len(sif_vars)>1:
            p_var = (p_vals<max([p_vals.max()-delta_p, max_p_val]))
        else:
            p_var = (p_vals<=1)
        
        
        # Probar el eliminar variables con coeficientes contradictorios
        reg_vars = pd.DataFrame(cie_model.params[1:], columns=['Coef'])
        coef_var = reg_vars[reg_vars.index.isin(neg_vars)] # solo inegi, contaminantes y poblacion
        var_ok = coef_var['Coef']
        var_ok = var_ok[var_ok<0]

        if all(p_var):        
            if var_ok.shape[0]>0 and len(sif_vars)>1:
                worst_var = p_vals[var_ok.index.values].sort_values(ascending=False).index[0]
                p_var[worst_var] = False

         

        keep_going = False
        if p_vals.var()<1e-4 and p_var.size>15:
            p_var = (p_vals>-1).cumsum()<=15 # Si todos los p-values son iguales, probablemente indica un error, mantener solo N variables
            keep_going = True
            
            
        # antes de cambiar las variables, calcular correlacion media para penalizar
        nv = len(sif_vars)
        avg_corr = 0
        if len(sif_vars)>1:
            avg_corr = y_corr.loc[sif_vars,sif_vars].abs()
            avg_corr = avg_corr[avg_corr<1].max().max()
            
        sif_vars = p_var.index[p_var]
        
        # Función objetivo a optimizar para elegir el mejor modelo
        cur_ic = (cie_model.aic)*(1+l_neg*var_ok.shape[0]/n_nvars)*(1+l_cor*avg_corr)

        
        
        if all(p_var):
            no_vars = sif_vars0[~sif_vars0.isin(sif_vars)].values
            new_var = np.array([no_vars[n_forw%no_vars.shape[0]]])
            sif_vars = np.unique(np.concatenate([sif_vars, new_var]))
            n_forw += 1

        if (cur_ic<best_ic and var_ok.shape[0]<=neg_v) or n_it==1:
            best_ic = cur_ic
            neg_v = var_ok.shape[0]
            best_reg_model = cie_model
            n_it_ch = n_it
            n_forw = 0 # reset the search with every new model
            
        removed_vars = p_var.index[~p_var]
        prev_ic = cur_ic
        n_it += 1



    best_p_vals = best_reg_model.pvalues[1:]
    while any(best_p_vals>max_p_val_final) and len(best_p_vals)>1:     
        sif_vars = best_p_vals.index[best_p_vals<best_p_vals.max()]
        sif_vars_f = '+'.join(sif_vars)
        
        best_reg_model = smf.glm(
            'Y~'+sif_vars_f,
            data=train,
            family=sm.families.NegativeBinomial()).fit()
        
        best_p_vals = best_reg_model.pvalues[1:]




    # Utilizar el modelo con los mejores valores encontrados
    cie_model = best_reg_model   

    pred_train = cie_model.fittedvalues
    pred_test = cie_model.predict(test)

    # Buscar outliers grandes
    idx_outlier = (pred_test>pred_test.quantile(0.75)*100)
    if any(idx_outlier):
        test = test[~idx_outlier]
        pred_test = pred_test[~idx_outlier]


    pred_err_train = np.abs(1-(pred_train.dot(train.Y))/(pred_train.dot(pred_train))) # abs(1-beta_regression) : (x'x)^-1 * x'y
    pred_err_test = np.abs(1-(pred_test.dot(test.Y))/(pred_test.dot(pred_test)))
    corr_test = np.corrcoef(test.Y, pred_test)[1,0]
        
    p_vals = cie_model.pvalues[1:]






    # stats
    cie_id.append(grp)
    cie_name.append(cie_x_desc)
    cie_reg_err.append(pred_err_test)
    cie_reg_cor.append(corr_test)

    reg_vars = pd.DataFrame(cie_model.params[1:], columns=['Coef'])
    cie_inegi_vars.append(reg_vars.index.isin(X_inegi_fa.columns).sum())
    cie_cont_vars.append(reg_vars.index.isin(X_cont_s.columns).sum())
    cie_emun_vars.append(reg_vars.index.str.contains('^E_MUN_', regex=True).sum())

    
    cie_negv.append((reg_vars[reg_vars.index.isin(neg_vars)]['Coef']<0).sum())
    cie_time.append(reg_vars.index.str.contains('FECHA').sum())
    cie_sexo.append(reg_vars.index.str.contains('REL_H_M').sum())
            
    cie_only_pobtot.append( int(any(reg_vars.index.str.contains('POBTOT')) and reg_vars.shape[0]==1) )
    cie_cronic.append( pd.Series(cie_x).isin(cie_c['cie']).mean() )
    cie_pred_outliers.append( idx_outlier.sum() )
    cie_n_cases.append( train.shape[0] + test.shape[0] )

    
    #------------------------------------------------------------------
    # Printing
    #------------------------------------------------------------------    
    
    # Se grefican los resultados

    if pred_err_test<1:        
    
        print(f'Negative Binomial Model [{grp} - {cie_x_desc}]')
        print(cie_model.summary())
        
        p_val = cie_model.pvalues[1:]
        reg_vars_n = pd.DataFrame(cie_model.params[1:].sort_values(ascending=False), columns=['Coef'])
        reg_vars_n = reg_vars_n.assign(Desc='')
        
        cie_in_reg = reg_vars_n.index[reg_vars_n.index.isin(cie.index)].values
        if cie_in_reg.shape[0]>0:
            reg_vars_n.loc[cie_in_reg,'Desc'] = cie.loc[cie_in_reg, 'Nombre']
            
            
        emun_vars = reg_vars_n.index.str.contains('^E_MUN_', regex=True)
        if emun_vars.sum()>0: 
            emun_vals = (reg_vars_n.index[emun_vars].str.extract(r'^E_MUN_(.*)', expand=True)+'0001').values.flatten()
            reg_vars_n.loc[emun_vars,'Desc'] = 'Residencia: ' + nom_ent[emun_vals].values

        month_vars = reg_vars_n.index.str.contains('^MES_', regex=True)
        if month_vars.sum()>0: 
            month_vals = (reg_vars_n.index[month_vars].str.extract(r'^MES_(.*)', expand=True)).values.flatten()
            reg_vars_n.loc[month_vars,'Desc'] = ['Mes de ' + month_en_es[i] for i in month_vals]

        
        if any('SEXO_M'==reg_vars_n.index):
            reg_vars_n.loc['SEXO_M','Desc'] = 'Sexo masculino'
        if any('EDAD'==reg_vars_n.index):
            reg_vars_n.loc['EDAD','Desc'] = 'Edad del paciente'
        if any('PESO'==reg_vars_n.index):
            reg_vars_n.loc['PESO','Desc'] = 'Peso del paciente'
        if any('FECHA'==reg_vars_n.index):
            reg_vars_n.loc['FECHA','Desc'] = 'Fecha de ingreso del paciente'
        if any('NO2_NOx'==reg_vars_n.index):
            reg_vars_n.loc['NO2_NOx','Desc'] = 'Contaminantes NO2 y NOX'
        if any('PM_CO'==reg_vars_n.index):
            reg_vars_n.loc['PM_CO','Desc'] = 'Contaminantes PM10, PM2.5 y CO'
        if any('SO2_NO_O3'==reg_vars_n.index):
            reg_vars_n.loc['SO2_NO_O3','Desc'] = 'Contaminantes SO2, NO y O3'
        if any('F_ECONOM'==reg_vars_n.index):
            reg_vars_n.loc['F_ECONOM','Desc'] = 'Factor Economico / Vivienda'
        if any('F_SOCIAL'==reg_vars_n.index):
            reg_vars_n.loc['F_SOCIAL','Desc'] = 'Factor Social'
    
        if any('POBTOT'==reg_vars_n.index):
            reg_vars_n.loc['POBTOT','Desc'] = 'Población total'
        if any('REL_H_M'==reg_vars_n.index):
            reg_vars_n.loc['REL_H_M','Desc'] = 'Hombres por cada 100 mujeres'
        if any('P_0A2'==reg_vars_n.index):
            reg_vars_n.loc['P_0A2','Desc'] = 'Población de 0 a 2 años'
        if any('P_18A24'==reg_vars_n.index):
            reg_vars_n.loc['P_18A24','Desc'] = 'Población de 18 a 24 años'
        if any('P_60YMAS'==reg_vars_n.index):
            reg_vars_n.loc['P_60YMAS','Desc'] = 'Población de 60 años y más'
        if any('POB0_14'==reg_vars_n.index):
            reg_vars_n.loc['POB0_14','Desc'] = 'Población de 0 a 14 años'
        if any('POB15_64'==reg_vars_n.index):
            reg_vars_n.loc['POB15_64','Desc'] = 'Población de 15 a 64 años'
        if any('POB65_MAS'==reg_vars_n.index):
            reg_vars_n.loc['POB65_MAS','Desc'] = 'Población de 65 años y más'
        if any('POB_AREA'==reg_vars_n.index):
            reg_vars_n.loc['POB_AREA','Desc'] = 'Densidad de población'
    
        par_lname = pd.DataFrame(reg_vars_n.index.values, columns=['Name'], index=reg_vars_n.index.values).copy()
        if CFG.lang=='EN':
            if any('SEXO_M'==reg_vars_n.index):
                reg_vars_n.loc['SEXO_M','Desc'] = 'Male sex'
            if any('EDAD'==reg_vars_n.index):
                reg_vars_n.loc['EDAD','Desc'] = 'Patient\'s age'
            if any('PESO'==reg_vars_n.index):
                reg_vars_n.loc['PESO','Desc'] = 'Patient\'s weight'
            if any('FECHA'==reg_vars_n.index):
                reg_vars_n.loc['FECHA','Desc'] = 'Patient\'s admission date'
            if any('NO2_NOx'==reg_vars_n.index):
                reg_vars_n.loc['NO2_NOx','Desc'] = 'Pollutants NO2 and NOX'
            if any('PM_CO'==reg_vars_n.index):
                reg_vars_n.loc['PM_CO','Desc'] = 'Pollutants PM10, PM2.5 and CO'
            if any('SO2_NO_O3'==reg_vars_n.index):
                reg_vars_n.loc['SO2_NO_O3','Desc'] = 'Pollutants SO2, NO and O3'
            if any('F_ECONOM'==reg_vars_n.index):
                reg_vars_n.loc['F_ECONOM','Desc'] = 'Economic Factor / Housing'
            if any('F_SOCIAL'==reg_vars_n.index):
                reg_vars_n.loc['F_SOCIAL','Desc'] = 'Social Factor'
        
            if any('POBTOT'==reg_vars_n.index):
                reg_vars_n.loc['POBTOT','Desc'] = 'Total Population'
            if any('REL_H_M'==reg_vars_n.index):
                reg_vars_n.loc['REL_H_M','Desc'] = 'Males per 100 females'
            if any('P_0A2'==reg_vars_n.index):
                reg_vars_n.loc['P_0A2','Desc'] = 'Population 0 to 2 y/o'
            if any('P_18A24'==reg_vars_n.index):
                reg_vars_n.loc['P_18A24','Desc'] = 'Population 18 to 24 y/o'
            if any('P_60YMAS'==reg_vars_n.index):
                reg_vars_n.loc['P_60YMAS','Desc'] = 'Population 60 y/o and over'
            if any('POB0_14'==reg_vars_n.index):
                reg_vars_n.loc['POB0_14','Desc'] = 'Population 0-14 y/o'
            if any('POB15_64'==reg_vars_n.index):
                reg_vars_n.loc['POB15_64','Desc'] = 'Population 15 to 64 y/o'
            if any('POB65_MAS'==reg_vars_n.index):
                reg_vars_n.loc['POB65_MAS','Desc'] = 'Population 65 y/o and over'
            if any('POB_AREA'==reg_vars_n.index):
                reg_vars_n.loc['POB_AREA','Desc'] = 'Population density'                    

            if emun_vars.sum()>0: 
                emun_vals = (reg_vars_n.index[emun_vars].str.extract(r'^E_MUN_(.*)', expand=True)+'0001').values.flatten()
                reg_vars_n.loc[emun_vars,'Desc'] = 'Residence: ' + nom_ent[emun_vals].values
    
            month_vars = reg_vars_n.index.str.contains('^MES_', regex=True)
            if month_vars.sum()>0: 
                month_vals = (reg_vars_n.index[month_vars].str.extract(r'^MES_(.*)', expand=True)).values.flatten()
                reg_vars_n.loc[month_vars,'Desc'] = ['Month of ' + month_en_es[i] for i in month_vals]
                month_idx_en = []
                [month_idx_en.append(f'MONTH_{i}') for i in month_vals]
                par_lname.Name[month_vars] = month_idx_en
                
                                
            if any('FECHA'==par_lname):
                par_lname.Name['FECHA'] = 'DATE'
            if any('PESO'==par_lname):
                par_lname.Name['PESO'] = 'WEIGHT'
            if any('EDAD'==par_lname):
                par_lname.Name['EDAD'] = 'AGE'
            if any('SEXO_M'==par_lname):
                par_lname.Name['SEXO_M'] = 'SEX_M'

            
        inegi_v_model.loc[inegi_v_model.index.isin(reg_vars_n.index),'count'] += 1
        cont_v_model.loc[cont_v_model.index.isin(reg_vars_n.index),'count'] += 1
        
        
        high_b_pars = reg_vars_n.loc[reg_vars_n.Coef>0,]
        low_b_pars = reg_vars_n.loc[reg_vars_n.Coef<0,]
        if high_b_pars.shape[0]>0:
            sorted_idx = np.argsort(high_b_pars.Coef)    
            high_b_pars = high_b_pars.iloc[sorted_idx[::-1],:]
            print('\nPrincipales variables que aumentan el número de hospitalizaciones:')
            print(high_b_pars)
        if low_b_pars.shape[0]>0:
            sorted_idx = np.argsort(low_b_pars.Coef)    
            low_b_pars = low_b_pars.iloc[sorted_idx,:]
            print('\nPrincipales variables que disminuyen el número de hospitalizaciones:')
            print(low_b_pars)
    
        
        print('\n')
        print(f'REG ERR para {grp} (Entrenamiento) :  {pred_err_train:.3}')
        print(f'REG ERR para {grp} (Validación)    :  {pred_err_test:.3}')
        print(f'REG COR para {grp} (Validación)    :  {corr_test:.3}')
        print('\n\n')
    
        
        max_feat = 20
        feature_importance = cie_model.params[1:]
        sorted_idx = np.argsort(feature_importance.abs())    
        pos = (np.arange(sorted_idx.shape[0]) + 0.5)[-max_feat:]
        par = feature_importance[sorted_idx][-max_feat:]
        
        clr = pd.Series(['#FF000099']*len(par))
        clr[(par<0).values] = '#0000FF99'

        size_y = 0
        if reg_vars_n.shape[0]>5:
            size_y = round((reg_vars_n.shape[0]-5)*0.5)
            
        fig = plt.figure(figsize=(10, 4+size_y))
        plt.barh(pos, par, align="center", color=clr)
        plt.yticks(pos, reg_vars_n.Desc[par.index]+'\n['+par_lname.Name[par.index].values+' | p-value: '+p_val[par.index].apply(lambda x: f'{x:.3f}').astype(str)+']')
        if CFG.lang=='EN':
            plt.title(f"{grp_en[grp]}\nFactors associated with an increase or decrease in the number of hospitalizations")
        else:
            plt.title(f"{grp} - {cie_x_desc}\nFactores asociados al aumento o disminución del número de hospitalizaciones")
        plt.subplots_adjust(left=0.25, right=0.99)
        if CFG.save_plot:
            plt.savefig(f'{CFG.out}/{CFG.grp}-{grp}_reg_nb_varimp-{CFG.lang}.png')
            plt.savefig(f'{CFG.out}/{CFG.grp}-{grp}_reg_nb_varimp-{CFG.lang}.pdf')




    
        #---------
        # Saving model
        #---------
        models_dict[grp+'_ERR'] = pred_err_test
        models_dict[grp+'_NB'] = cie_model
        models_dict[grp+'_xmin'] = xmin
        models_dict[grp+'_xmax'] = xmax
        models.append(grp)
        
        model_vars = pd.concat([reg_vars_n.Desc, model_vars], axis=0)

#------------------------------------------------------------------
# Resultados
#------------------------------------------------------------------    
#
# Se guardan los modelos y sus medidas de desempeño
#
cie_mod_stats = pd.DataFrame(data={'id':cie_id,'name':cie_name,
                   'inegi_vars':cie_inegi_vars,'cont_vars':cie_cont_vars,
                   'emun':cie_emun_vars,
                   'reg_err':cie_reg_err, 'reg_cor':cie_reg_cor, 'time':cie_time, 
                   'sexo_m':cie_sexo, 'neg_v':cie_negv, 
                   'only_pobtot':cie_only_pobtot, 
                   'cronic':cie_cronic, 'pred_outliers':cie_pred_outliers,
                   'n_cases':cie_n_cases})

real_n_cie = cie_mod_stats.shape[0]


# Summary
print('\n\n\n')
print(f'CIE                   :       ERR')
for i in models:
    print(f"{i} - {cie_grp_desc[i]}:   {models_dict[i+'_ERR']:.3}")

print(f"REG MEAN ERR:   {cie_mod_stats.reg_err.mean():.3}")
print(f"REG MEAN COR:   {cie_mod_stats.reg_cor.mean():.3}")



model_vars.drop_duplicates(inplace=True)
model_vars.sort_index(inplace=True)

# modelos y variables
models_dict['models'] = models
models_dict['model_vars'] = model_vars
models_dict['models_name'] = df_grp.desc[models]
models_dict['affec_name'] = cie.loc[model_vars[pd.Series(model_vars).isin(cie.index)],'Nombre']
models_dict['model_stats'] = cie_mod_stats
models_dict['inegi_vars'] = inegi_v_model
models_dict['cont_vars'] = cont_v_model
models_dict['inegi_vars_cie'] = inegi_loc.columns
models_dict['cont_vars_cie'] = cont_loc.columns
models_dict['grp_data'] = df_grp

# Se guardan los modelos para ser utilizados en los sistema web para la modelización del riesgo (dashboards)
with open('n_hosp.pickle', 'wb') as handle:
    pickle.dump(models_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
