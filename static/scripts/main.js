// *** About area functions
function getElementNumber() {
    //var test = document.querySelector("#filter > li:nth-child(" + index + ")");
    // try {
    //  var x = getAttribute(AttributeName, Value);
    //}
    // catch (err) {
    //  test.setAttribute(AttributeName, Value);
    // }
    elements = ["features", "changelog", "other"];
    return elements.length;
}
function showElement(element, index) {
    clearView();
    ActivateElement(element, "block");
    DeactivateAllElement();
    document.querySelector("#filter > li:nth-child(" + index + ")").classList.add("active");

}
function clearView() {
    
    //for (let i = 0; i < names.length; i++) { console.log(names[i].innerText); }

    for (var i = 0; i < getElementNumber();i++) {
        try {
            SetElementStyleByID(elements[i], "none");
        }
        catch (err) { }
    }
}
function DeactivateAllElement() {
    try {
        for (var i = 1; i <= getElementNumber(); i++) {
            document.querySelector("#filter > li:nth-child(" + i + ")").classList.remove("active");
        }
    }
    catch (err) { console.log("[DEBUG] Element exception: " + i); }
}

function ActivateElement(name, mode) {
    SetElementStyleByID(name, mode);
}


// *** Tracking area

function privacy_banner_check() {
    if (localStorage.getItem("analytics_tracking")) {
        SetElementStyleByID("privacy_policy", "none");
    }
}

function hideMessage() {
    if (localStorage.getItem("analytics_tracking")) {
        setLocalStorage("message_hidden", "true");
    }
}
function enableTracking() {
    setLocalStorage("analytics_tracking", "true")
    window.location = "/";
}

function disableTracking() {
    setLocalStorage("analytics_tracking", "false")
    window.location = "/";
}

// *** Custom Code Wrappers, maintain them here in case of an upgrade.

function SetElementStyleByID(id, style)
{
    document.getElementById(id).style.display = style;
}

function setLocalStorage(key, value) {
    localStorage.setItem(key, value);
    console.log("LocalStorage Value set: " + key + value);
}
