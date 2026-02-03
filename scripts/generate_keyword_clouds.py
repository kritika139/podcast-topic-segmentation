import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

keywords_path = "../dataset/topic_keywords"
output_path = "../output/keyword_clouds"

os.makedirs(output_path, exist_ok=True)

for file in os.listdir(keywords_path):
    if file.endswith("_keywords.txt"):
        with open(os.path.join(keywords_path, file), "r", encoding="utf-8") as f:
            text = f.read().replace(",", " ")

        wc = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(text)

        plt.figure(figsize=(8, 4))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")

        plt.savefig(f"{output_path}/{file.replace('.txt', '.png')}")
        plt.close()

print("✅ Keyword clouds generated")
