import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("shopping_trends_updated.csv")



#***************************************************************** en çok alışveriş yapan 12 yer
#'Location' sütununu ayrıştırarak her bir ülkeyi ayrı bir satırda temsil eden DataFrame'i oluşturun
df_ayristirilmis = df['Location'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).reset_index()
df_ayristirilmis.columns = ['Index', '']

# En çok geçen 10 ülkeyi bulun
en_cok_gecen_10_ulke = df_ayristirilmis[''].value_counts().nlargest(12)

en_cok_gecen_10_ulke.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='Paired')

# Grafiği düzenleme
plt.title('En Çok Geçen 12 Bölge ')

# Grafik penceresini göster
plt.show()

#******************************************************



#****************************************************
# erkeklerin en çok aldığı ürünler
erkek_verisi = df[df['Gender'] == 'Male']

# Kadınların ne aldığını görelim
en_cok_alinan_kiyafet = erkek_verisi['Item Purchased'].value_counts().nlargest(12)

# Sonuçları yazdıralım
print(en_cok_alinan_kiyafet)
en_cok_alinan_kiyafet.plot(kind='bar', color='skyblue')
plt.title('Erkeklerin  En Çok Aldığı 12 Kıyafet Türü')
plt.xlabel('Kıyafet Türü')
plt.ylabel('Adet')
plt.show()

#****************************************



#********************************************************

#kadınlar en çok hangi ödeme yöntemi ile ödeme yapmış
kadın_verisi = df[df['Gender'] == 'Male']

# Kadınların en çok kullandığı ödeme yöntemini bulalım

en_cok_kullanilan_odeme_yontemii = kadın_verisi['Payment Method'].value_counts()

# Sonucu yazdıralım
print(f"Kadınların en çok kullandığı ödeme yöntemi: {en_cok_kullanilan_odeme_yontemii}")

#*****************************************************



#*************************

# yaş kategorisi ekledik 

df['Yaş Kategorisi'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 50, float('inf')],
                               labels=['Çocuk', 'Genç', 'Genç Yetişkin', 'Orta Yaşlı', 'Yaşlı'])
df.insert(2, 'Yaş Kategorisi', df.pop('Yaş Kategorisi'))

print(df)

#***************************************


#yeni kolon toplam alışveriş tutarı 
df['Toplam Alışveriş Tutarı'] = df.groupby('Customer ID')['Purchase Amount (USD)'].transform('sum')
df['Toplam Alışveriş Tutarı'] = df['Toplam Alışveriş Tutarı'].apply(lambda x: f'${x:.2f}')



# yaş kategorisi grafiği

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


# yaş grubuna göre en çok ne almış onun grafiği
en_cok_alinan_urunler = df.groupby('Yaş Kategorisi')['Item Purchased'].agg(lambda x: x.mode().iloc[0])


plt.figure(figsize=(10, 6))
sns.countplot(x='Yaş Kategorisi', hue='Item Purchased', data=df, palette='viridis')
plt.title('Yaş Kategorilerine Göre Satın Alınan Ürünler')
plt.xlabel('Yaş Kategorisi')
plt.ylabel('Müşteri Sayısı')
plt.legend(title='Item Purchased', bbox_to_anchor=(1, 1))
plt.show()