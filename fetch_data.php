<?php
header('Content-Type: application/json');

$host = 'localhost';
$user = 'root';
$password = '';
$database = 'testscarping';

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die('Database connection failed: ' . $conn->connect_error);
}

// Get page and limit parameters
$page = isset($_GET['page']) ? (int)$_GET['page'] : 0;
$limit = isset($_GET['limit']) ? (int)$_GET['limit'] : 2000;
$offset = $page * $limit;

$sql = "SELECT `Service ID` AS service_id, 
               `Service Name` AS service_name, 
               `Rate per Thousand` AS rate_per_thousand, 
               `Minimum Quantity` AS min_quantity, 
               `Maximum Quantity` AS max_quantity, 
               `Average Time` AS avg_time, 
               `Category of the Service` AS category, 
               `provider`, 
               `Description` AS details 
        FROM scarpedata
        LIMIT $limit OFFSET $offset";

$result = $conn->query($sql);

$data = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
}

echo json_encode($data);
$conn->close();
?>
