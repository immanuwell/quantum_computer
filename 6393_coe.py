import streamlit as st
import cv2
import numpy as np
from PIL import Image

def draw_circle(image, center_x, center_y, radius):
    cv2.circle(image, (center_x, center_y), radius, (0, 0, 255), 2)

def main():
    st.title("Web-приложение для рисования окружностей")

    # Загрузка изображения
    img_map = np.array(Image.open("img_map.png"))  # Загрузка изображения в массив numpy

    st.image(img_map, channels="RGB")

    num_centers = st.slider("Выберите количество центров (от 1 до 5)", 1, 5, 2)

    center_x_list = []
    center_y_list = []

    coords = ((1016, 20), (2456, 1412))
    for i, coor in zip(range(num_centers), coords):
        center_x = st.slider(f"Выберите координату X для центра {i+1}", 0, img_map.shape[1], coor[0])
        center_x_list.append(center_x)
        center_y = st.slider(f"Выберите координату Y для центра {i+1}", 0, img_map.shape[0], coor[1])
        center_y_list.append(center_y)

    # Ползунки для выбора диапазона радиуса окружностей
    start_radius = st.slider("Начальный радиус", 1, 100, 7)
    end_radius = st.slider("Конечный радиус", start_radius, 3000, 2800)
    step_radius = st.slider("Шаг радиуса", 1, 1000, 779)

    # Отрисовка окружностей
    for center_x, center_y in zip(center_x_list, center_y_list):
        for radius in range(start_radius, end_radius + 1, step_radius):
            draw_circle(img_map, center_x, center_y, radius)

    # Отображение изображения с нарисованными окружностями
    st.image(img_map, channels="RGB")

if __name__ == "__main__":
    main()
