import pywhatkit as kit
import time

def send_whatsapp_with_image(to, image_path):
    try:
        kit.sendwhats_image(to, image_path, caption="Respected sir/madam, please find your ward's report attached.")
        time.sleep(10)
        return True
    except Exception as e:
        print(f"Error occurred while sending: {e}")
        return False