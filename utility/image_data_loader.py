import numpy as np
from PIL import Image, ImageOps


class ImageDataLoader:
    @staticmethod
    def load_background_image_data(path, width, height):
        try:
            image = Image.open(path)
            resized_image = image.resize((width, height))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_force_fit_full_screen_image_data(path, width, height):
        try:
            image = Image.open(path)

            # 이미지를 화면 크기에 맞게 확장
            resized_image = ImageOps.fit(image, (width, height), method=0, bleed=0.1, centering=(0.5, 0.5))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_battle_field_card_frame_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((105, 170))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_card_frame_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((570, 916))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_rectangle_origin_image_data(path):
        try:
            image = Image.open(path)
            rgba_image = image.convert("RGBA")
            img_data = np.array(rgba_image)

            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_lanczos_resized_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((300, 250), Image.LANCZOS)

            # rgba_image = resized_image.convert("RGBA")
            # img_data = np.array(rgba_image)
            # resized_image.close()
            # image.close()

            return resized_image

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_message_on_the_battle_screen_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((2278, 231))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_rectangle_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((300, 300))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_surrender_screen_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((1200, 600))

            rgba_image = resized_image.convert("RGBA")
            img_data = np.array(rgba_image)

            resized_image.close()
            image.close()

            return img_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_oval_image_data(image_path):
        try:
            image = Image.open(image_path)
            width, height = image.size
            image_data = image.tobytes("raw", "RGB", 0, 0)

            image.close()

            return width, height, image_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_circle_image_data(image_path):
        try:
            image = Image.open(image_path)
            width, height = image.size
            image_data = image.tobytes("raw", "RGB", 0, 0)

            image.close()

            return width, height, image_data

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None

    @staticmethod
    def load_shop_card_lanczos_resized_image_data(path):
        try:
            image = Image.open(path)
            resized_image = image.resize((800, 400), Image.LANCZOS)

            # rgba_image = resized_image.convert("RGBA")
            # img_data = np.array(rgba_image)
            # resized_image.close()
            # image.close()

            return resized_image

        except Exception as e:
            print(f"Error loading image data: {e}")
            return None