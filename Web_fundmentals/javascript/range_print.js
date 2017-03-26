function printRange(start,end,skip){
  
  var i=start;
  
  if(start && end && skip){
    
    while(i<end){
      console.log(i);
      i=i+skip;
    }
  }
  
  
  if(start && end && !skip){
    var skip=1;
    
    while(i<end){
      console.log(i);
      i=i+skip;
    }
  }
  
  if(start && !end && !skip){
    
    for(var i=0;i<start;i++){
      console.log(i);
    }
  }
  

}

printRange(-2,10,2);
printRange(4,8);
printRange(4);