a nearula netwokr is a compurational model designed to mimic how the human brain works by procss information , recognize pattersnand make decision . it consitns of layesr of interconnected nodes or neurons , that work together to analyze data , make predictions or classify inputs . 


## key components of a neural network 

- neurons(nodes): the basic units that process information . each neuron takes inputs , processes them and passes the output to the next layer . 

- layers : nerual networks are strucred in layers: 
    - input layer: receives that raw data ( images, text ,numbes)
    - hidden layers : perform computations, often multple layers in deep neural networks . 
    - output layer : process the final ouput which could be a categoriy or a umerical value . 
## weights :
 each connection between neurons has a weight that determines the influence of one neron on another . the network learns by adjusting these weights . 

## activation funtion:
 a mathematical funtion applied to each neron outpu to intorduce non -inearity , which allows the network to leanr complex patterns . 

## how a neral network works 

the nerual network works throught a process called forwad propagation and backpropagation.

- forward propagation:
    - data enters the network throth the iput layer
    - each neuron in a layer processes its inptu applying weights and an activation funion . 
    - the processed data moes throught each layer until it reaches the output layer wehre a result is produced. 


## calulating loss 

- the output from the forwad propagation is compared to the actual anser using a loss funtion , whch calcuates teh error or loss of the prediction. 

## backpropagraion :
- the network then uses backpropagation , a process that adjsusts weights to minimize the error. 
- the erro from the output is sent back throught the network and each weight is udated slightly to reduce the error.
- over many iterations the network learns to reduce the loss improvin its accuracy. 

## trainign a nerual network 

the trainng process invloves 
- feeding data throught the network 
- calcuating the error
- adjusting via bckprogpagation to reduce the errro 
- repeating the process on large datasets ( often thousanda or miliions of times to reach an optimal model )

## types of nerual networks 

there are different types of nerula networks taileored for various tasks: 

- feedforward neural networks : information flows in one direction, useful for general taks like classification . 

- convolutional neral netwroks (CNNs) : designed for image processing .CNNS detect spatial hierarches in images . 
- recurrent nerual networks ( RNNs): desiged for sequenctal data, like time seres or lannguage , wehre past inputs influence the current output. 
- tranformer networks : primarily usedin natural language processing , tranformers use attention mechanisms to handle relationships between words effectively . 

