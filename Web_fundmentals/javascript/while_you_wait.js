var daysUntilMyBirthday = 30;

function while_you_wait(){
  
    for (var i=0; i<daysUntilMyBirthday+1;i++){
      if(i>=30){
        console.log(i+"Days until my birthday. Such a long time")
      }
      
      if(i<30 && i>5){
        console.log(i+"Days until my birthday. Birthday is comming soon");
      }
      if(i<=5 && i>0){
        console.log(i+"Days until my birthday. I am excited....la la la");
      }
      
       if(i==0){
        console.log("Let's have party ...........");
      }
      
    }
    
  }

while_you_wait(daysUntilMyBirthday);