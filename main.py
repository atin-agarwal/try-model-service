import pickle
import sys

# load the model from disk
modelFileName = sys.argv[1]
loaded_model = pickle.load(open(modelFileName, 'rb'))

inputFileName = sys.argv[2]
with open(inputFileName, 'r') as myfile:
        data = myfile.readlines()
        print("Input data :: ", data)

x1=int(data[0].replace('\n', ''))
x2=int(data[1].replace('\n', ''))
x3=int(data[2].replace('\n', ''))

X_TEST = [[x1,x2,x3]]
outcome = loaded_model.predict(X=X_TEST)
print ('Result :: ', outcome)
