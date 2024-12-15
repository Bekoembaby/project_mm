import tkinter as tk
from playsound import playsound
from gtts import gTTS
import os
from threading import Thread

audio_file = "output.mp3"
playing = False

# تشغيل الصوت في خيط مستقل
def play_audio():
    global playing
    try:
        playsound(audio_file)
    except Exception as e:
        result_label.config(text=f"حدث خطأ أثناء التشغيل: {e}")
    finally:
        playing = False

def text_to_speech():
    global playing

    text = text_input.get("1.0", "end-1c")  # قراءة النص من مربع الإدخال
    if not text.strip():
        result_label.config(text="من فضلك أدخل نصاً")
        return

    try:
        # إذا كان الملف الصوتي موجودًا، نقوم بحذفه
        if os.path.exists(audio_file):
            os.remove(audio_file)

        # تحويل النص إلى صوت باستخدام gTTS
        tts = gTTS(text=text, lang='ar')
        tts.save(audio_file)  # حفظ الصوت كملف MP3
        result_label.config(text="تشغيل الصوت...")
        
        if not playing:
            playing = True
            Thread(target=play_audio).start()  # تشغيل الصوت في خيط منفصل
    except Exception as e:
        result_label.config(text=f"حدث خطأ: {e}")

if __name__ == "__main__":
    # إنشاء نافذة البرنامج
    root = tk.Tk()
    root.title("برنامج تشغيل الصوت")
    root.geometry("400x400")  # تعديل حجم النافذة إذا كان الزر مغطى
    root.resizable(False, False)

    # عناصر الواجهة الرسومية
    label = tk.Label(root, text="أدخل النص الذي تريد تشغيله كصوت:", font=("Arial", 14))
    label.pack(pady=10)

    text_input = tk.Text(root, height=8, width=40, font=("Arial", 12))
    text_input.pack(pady=10)

    convert_button = tk.Button(root, text="تشغيل الصوت", command=text_to_speech, font=("Arial", 12), bg="#4CAF50", fg="white")
    convert_button.pack(pady=10)


    result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
    result_label.pack(pady=10)

    # تشغيل البرنامج
    root.mainloop()
