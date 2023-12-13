from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format='png')

# Set graph attributes for side by side layout
dot.attr(rankdir='LR')

# Set global node and edge attributes for font
dot.attr('node', fontname='Roboto', fontsize='7')
dot.attr('edge', fontname='Roboto', fontsize='7')

# Add nodes with labels
dot.node('A', 'Raw Data\n(Optical Illusions)')
dot.node('B', 'Human Annotator\n(Perception)')
dot.node('C', 'Annotated Data\n(Labels)')
dot.node('D', 'Generative Models')

# Add edges with labels
dot.edge('A', 'B', label='Meticulous Annotation')
dot.edge('B', 'C', label='Capture Nuances')
dot.edge('C', 'D', label='Enhance Models')

# Add loop back from 'D' to 'A'
dot.edge('D', 'A', label='Perceptional AI')

# Render the graph to a file
dot.render('/Users/meltemballan/Documents/Image_Processing/images/flowchart_illusion_loop.png')