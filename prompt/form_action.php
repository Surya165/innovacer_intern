<?php
if(isset($_POST['submit']))
{
  $email = $_POST['email'];
  $series = $_POST['series'];
  if(!isset($email))
  {
    echo "Enter a valid email";
  }
  if(!isset($series))
  {
    echo "Enter atleast one series name";
  }
  $input = "Email address: ";
  $input.= $email."\n";
  $input .="Tv series: ";
  $input.= $series."\n";
  $file = fopen("../database/input.txt","w");
  fwrite($file,$input);
  fclose($file);
  $msg = exec("python3 ../database/dumpDatabase.py");
  //echo "<p margin-top='400px'>".$msg."</p>";
}
 ?>
