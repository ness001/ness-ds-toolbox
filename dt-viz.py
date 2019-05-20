from sklearn.tree import export_graphviz export_graphviz(model,out_file='rf.dot',feature_names=name,
   class_names=y_str,rounded=True,proportion=True,
              precision=2,filled=True)
from subprocess import call
call([r'C:\Program Files (x86)\Graphviz2.38\bin\dot.exe',
     '-Tpng','rf.dot','-o','rf.png','-Gdpi=600'])
from IPython.display import Image
Image(filename='rf.png')
preds=model.predict(X)

#method 2
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydot 
dot_data=StringIO()
tree.export_graphviz(model,out_file=dot_data,
                    feature_names=X_train.columns,
                    class_names=['not survived','survived'],
                    filled=True,rounded=True,
                    special_characters=True
)
#pydot v1.2.0+
(graph,)=pydot.graph_from_dot_data(dot_data.getvalue())
#pydot v1.0-
graph=pydot.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())