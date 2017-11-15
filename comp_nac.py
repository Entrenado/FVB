datos = pd.read_csv('competencia2.txt', sep='\t', encoding='latin-1')
datos.describe()
datos.columns= ['Column1', 'Club', 'FedAut', 'Tot_puntos', 'J2017', 'J2016',
       'J2015', 'J2014', 'TOTALJUNIOR', 'C2017', 'C2016', 'C2015',
       'C2014', 'TOTALCADETE', 'I2017', 'I2016', 'I2015', 'I2014',
       'TOTALINF']
jun_cad = datos[['TOTALJUNIOR', 'TOTALCADETE']]
jun_cad.fillna(0, inplace=True)
lista_cadete = ['C2017', 'C2016', 'C2015','C2014', 'TOTALCADETE']
lista_junior = ['J2017', 'J2016','J2015', 'J2014', 'TOTALJUNIOR']
datos_eusk = datos.loc[datos['FedAut'] == 'EUSKADI']
for n in lista_junior:
    for k in lista_cadete:
        df = datos[[n,k]]
        df2 = datos_eusk[[n,k]]
        print n, k, df[n].corr(df[k]), df2[n].corr(df[k])

        