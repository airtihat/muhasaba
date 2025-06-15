<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $plan = htmlspecialchars($_POST["plan"]);

    $subject = "تأكيد الاشتراك - شركة المحاسبة السحابية";
    $message = "مرحبًا $name،\n\nتم استلام اشتراكك في باقة $plan بنجاح.\n\nشكرًا لاختيارك خدمتنا.\n";
    $headers = "From: noreply@yourcompany.com";

    // إرسال البريد
    if (mail($email, $subject, $message, $headers)) {
        header("Location: thank-you.html");
        exit();
    } else {
        echo "حدث خطأ أثناء إرسال البريد. يرجى المحاولة لاحقًا.";
    }
}
?>

