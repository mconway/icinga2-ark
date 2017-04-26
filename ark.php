<?php
if(!array_key_exists(1, $argv)){
  echo "Ip address is required";
  exit(1);
}

$ipAddress = $argv[1];

if(!array_key_exists(2, $argv)){
  $port = 27015;
}else{
  $port = $argv[2];
}

$response = file_get_contents("http://arkservers.net/api/query/{$ipAddress}:{$port}");
if($response === "null"){
  echo "Server is Offline\n";
  exit(1);
}

$serverData = json_decode($response);
echo "{$serverData->info->HostName}: {$serverData->info->Players}/{$serverData->info->MaxPlayers}\n";
exit(0);
