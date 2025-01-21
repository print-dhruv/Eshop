  // password show and hide logic
  function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const fieldType = passwordField.getAttribute("type");
    passwordField.setAttribute("type",fieldType === "password" ? "text" : "password");
  }