import dircache
import speech_recognition as sr
import pdb
import re
r = sr.Recognizer()


def get_filenames(ListPath):
    FileList=[];audio
    with open(ListPath) as fp:
        for line in fp:
            FileList.append(line.strip("\n"));
    return FileList;
     
	 
List = get_filenames("File_Input.txt")    
fo = open("Transcript.txt", "w")

for index in range(len(List)):
    with sr.WavFile(List[index]) as source:     # use "test.wav" as the audio source
         = r.record(source)                     # extract audio data from the file
        try:
            ASR_Result=r.recognize_google(audio, language='en-US')
            print(str(index) +": "+ ASR_Result.encode("utf-8"))   # recognize speech using Google Speech Recognition
            fo.write(ASR_Result.encode('utf8')+"\n")
        except:
			print("Google Speech Recognition could not understand audio")
			fo.write("Google Speech Recognition could not understand audio"+"\n")
fo.close()