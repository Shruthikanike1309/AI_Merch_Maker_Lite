<?php
header('Content-Type: application/json');
function log_message($msg) {
    error_log("[" . date('Y-m-d H:i:s') . "] $msg\n", 3, __DIR__ . '/../assets/generated/publisher.log');
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Only POST allowed']);
    exit;
}
$input = file_get_contents('php://input');
$data = json_decode($input, true);
if (!$data) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid JSON']);
    exit;
}
log_message('Received product publish request: ' . json_encode($data));
$product_id = 'MOCK' . rand(10000, 99999);
$response = [
    'status' => 'success',
    'product_id' => $product_id,
    'received_at' => date('c')
];
echo json_encode($response);
