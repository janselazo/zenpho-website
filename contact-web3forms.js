(function () {
  var form = document.getElementById("zenpho-contact-form");
  if (!form) return;

  var successEl = document.getElementById("zenpho-contact-success");
  var errorEl = document.getElementById("zenpho-contact-error");
  var submitBtn = form.querySelector('button[type="submit"]');
  var defaultBtnHtml = submitBtn ? submitBtn.innerHTML : "Submit";

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (errorEl) {
      errorEl.style.display = "none";
      errorEl.textContent = "";
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "Sending…";
    }

    fetch("https://api.web3forms.com/submit", {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    })
      .then(function (res) {
        return res.json().then(function (data) {
          return { ok: res.ok, data: data };
        });
      })
      .then(function (result) {
        if (!result.ok || !result.data.success) {
          throw new Error(
            (result.data && result.data.message) ||
              "Something went wrong. Please try again.",
          );
        }
        form.style.display = "none";
        if (successEl) successEl.style.display = "block";
      })
      .catch(function (err) {
        if (errorEl) {
          errorEl.textContent =
            err && err.message
              ? err.message
              : "Something went wrong. Please try again.";
          errorEl.style.display = "block";
        }
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = defaultBtnHtml;
        }
      });
  });
})();
