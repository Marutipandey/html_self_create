<?php 
if(isset($_POST['submit']))
{
    
    // Collecting User data

  $User_Name  = $_POST['User_Name'];
  $User_Email  =  $_POST['User_Email'];
  $User_Mobile  =   $_POST['User_Mobile'];
  $User_Msg  =   $_POST['User_Msg'];
 
   //   sending mail to rainet

  $to      = 'atmbank2021@gmail.com';
  $subject = 'New Client Query';
  $headers = 'From:' .$User_Email      . "\r\n" .
             'Reply-To: atmbank2021@gmail.com' . "\r\n" .
             'X-Mailer: PHP/' . phpversion();
  $headers .= "MIME-Version: 1.0\r\n";
  $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
  $message = '<p><strong> Clint Name :'.$User_Name.'</strong></p>
              <p><strong> Clint Mobile No :'.$User_Mobile.'</strong></p>
              <p><strong> Clint Message :'.$User_Msg.'</strong></p>';
            
 mail($to, $subject, $message, $headers);
 
 header("Location: thank.html");
 
}
?>