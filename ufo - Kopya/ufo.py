import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("shopping_trends_updated.csv")
#print(df)
print(df[df['Age']<30]) # yaşı 30dan küçükleri getirir
#print(df)
# print(df.drop("Promo Code Used",axis = 1)) # siler
# print(df.loc[3][0]) 3ün 1. değerini ver
print(df["Age"] < 1) 
yasortalama=df.Age.mean()
print(yasortalama)

sutun_adlari = df.columns
print("Sütun Adları:", sutun_adlari)
ad_sutunu = df['Location']

    

df['Yaş Kategorisi'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 50, float('inf')],
                               labels=['Çocuk', 'Genç', 'Genç Yetişkin', 'Orta Yaşlı', 'Yaşlı'])
df.insert(2, 'Yaş Kategorisi', df.pop('Yaş Kategorisi'))


# Seaborn kütüphanesini kullanarak yaş kategorilerini gösteren bir grafik oluşturalım
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(x='Yaş Kategorisi', data=df, palette="viridis")
plt.title('Yaş Kategorileri Grafiği')
plt.xlabel('Yaş Kategorisi')
plt.ylabel('Müşteri Sayısı')
plt.show()

en_cok_alinan_urunler = df.groupby('Yaş Kategorisi')['Item Purchased'].agg(lambda x: x.mode().iloc[0])

print(en_cok_alinan_urunler)

en_cok_alinan_urunler = df.groupby('Yaş Kategorisi')['Item Purchased'].agg(lambda x: x.mode().iloc[0])


plt.figure(figsize=(10, 6))
sns.countplot(x='Yaş Kategorisi', hue='Item Purchased', data=df, palette='viridis')
plt.title('Yaş Kategorilerine Göre Satın Alınan Ürünler')
plt.xlabel('Yaş Kategorisi')
plt.ylabel('Müşteri Sayısı')
plt.legend(title='Item Purchased', bbox_to_anchor=(1, 1))
plt.show()