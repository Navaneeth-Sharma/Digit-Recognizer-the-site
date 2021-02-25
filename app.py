from flask import Flask, render_template, request,redirect
# import numpy as np 
import os
# import librosa
import datetime
# from scipy.io.wavfile import write
# import sounddevice as sd
# import keras
# from keras import backend as K


app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Index():
    return render_template("index.html")

# def wav2mfcc(file_path, max_len=8):
#     wave, sr = librosa.load(file_path, mono=True, sr=16000)
#     amplitude = []
#     for i in wave:
#         if abs(i)>0.009:
#             amplitude.append(i)
#     mfcc = librosa.feature.mfcc(np.asarray(amplitude))

#     # If maximum length exceeds mfcc lengths then pad the remaining ones
#     if (max_len > mfcc.shape[1]):
#         pad_width = max_len - mfcc.shape[1]
#         mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')

#     # Else cutoff the remaining parts
#     else:
#         mfcc = mfcc[:, :max_len]
    
#     return mfcc


@app.route('/dataset', methods = ['GET','POST'])
def dataset():
    if request.method == 'POST':
        
#         color = "text-success"
#         messege = "Model predicts the spoken digit is"

#         return render_template('index.html',messege = messege, color=color)
        
#         if request.form.validate_on_submit():
#         if 'Record' in request.form:
#             freq = 22500
#             duration = 3
#             recording = sd.rec(int(duration * freq),  
#                    samplerate=freq, channels=2)
#             sd.wait() 

#             print(recording)
#             try:
#                 os.mkdir('data/')
#             except:
#                 pass

#             # write('data/hi1.wav',freq,np.asarray(recording,dtype=np.int16))
            
#             t1 = datetime.datetime.now() 

#             write('data/'+str(t1)+'.wav', freq, recording) 
#             print('------------------------------------------------------------------------------')

#             two = wav2mfcc('data/'+str(t1)+'.wav')
#             # print(two.shape)

#             model = keras.models.load_model('SRD')
#             out = model.predict_classes(np.array([np.asarray(two).reshape(20,8,1),]))
            
#             K.clear_session()
#             color = "text-success"
#             messege = "Model predicts the spoken digit is "+str(out[0])+" !!!"
            
#             return render_template('index.html',messege = messege, color=color)

        

            
        if request.files:

            try:
                os.mkdir('data/')
                
                color = "text-success"
                messege = "data folder created successfully"

#             
            except:
                pass
            
            audio = request.files['audio']

            t1 = datetime.datetime.now()
            audio.save('data/'+str(t1)+'.wav')
            
            messege+=" and also saved"
            
            
            return render_template('index.html',messege = messege, color=color)


#             two = wav2mfcc('data/'+str(t1)+'.wav')
#             print(two.shape)

#             model = keras.models.load_model('SRD')
#             out = model.predict_classes(np.array([np.asarray(two).reshape(20,8,1),]))
            
#             K.clear_session()
#             color = "text-success"
#             messege = "Model predicts the spoken digit is "+str(out[0])+ " !!!"
            
#             return render_template('index.html',messege = messege, color=color)
            
        # try:
        #     os.mkdir('data/')
        # except:
        #     pass
        # print(audio)
        # # audio = request.form.get('audio')
        # # data1, sr1 = librosa.load(audio)
        # # print(data1)

            # return redirect(request.url)


    return render_template('index.html')

if __name__ == '__main__':
    app.run()
