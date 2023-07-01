const profileStatus = document.currentScript.getAttribute('data-status');
const csrfToken = document.currentScript.getAttribute('csrfToken');

$(document).ready(function() {
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  const popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
    const popover = new bootstrap.Popover(popoverTriggerEl, {
      html: true,
      content: function() {
        const popoverContent = document.createElement('form');
        popoverContent.classList.add('d-flex', 'gap-2', 'flex-column');
        popoverContent.action = "update_profile_status";
        popoverContent.method = "POST"; // Set the form's method to POST

        // Add CSRF token input field
        const csrfTokenInput = document.createElement('input');
        csrfTokenInput.type = 'hidden';
        csrfTokenInput.name = 'csrfmiddlewaretoken';
        csrfTokenInput.value = csrfToken; // Use the provided CSRF token
        popoverContent.appendChild(csrfTokenInput);

        const onlineButton = document.createElement('button');
        onlineButton.className = 'btn bg-green border-0 text-white light-hover';
        onlineButton.innerText = 'Online';
        onlineButton.value = 'online'; // Set the button value to the corresponding status

        const inactiveButton = document.createElement('button');
        inactiveButton.className = 'btn bg-orange border-0 text-white light-hover';
        inactiveButton.innerText = 'Inactive';
        inactiveButton.value = 'inactive'; // Set the button value to the corresponding status

        const dndButton = document.createElement('button');
        dndButton.className = 'btn bg-red border-0 text-white light-hover';
        dndButton.innerText = "Don't Disturb";
        dndButton.value = 'dnd'; // Set the button value to the corresponding status

        const offlineButton = document.createElement('button');
        offlineButton.className = 'btn bg-gray border-0 text-white light-hover';
        offlineButton.innerText = 'Offline';
        offlineButton.value = 'offline'; // Set the button value to the corresponding status

        switch (profileStatus) {
          case 'online':
            onlineButton.classList.add('disabled');
            break;
          case 'inactive':
            inactiveButton.classList.add('disabled');
            break;
          case 'dnd':
            dndButton.classList.add('disabled');
            break;
          case 'offline':
          case '':
            offlineButton.classList.add('disabled');
            break;
        }

        popoverContent.appendChild(onlineButton);
        popoverContent.appendChild(inactiveButton);
        popoverContent.appendChild(dndButton);
        popoverContent.appendChild(offlineButton);

        // Submit form on button click
        [onlineButton, inactiveButton, dndButton, offlineButton].forEach(function(button) {
          button.addEventListener('click', function() {
            const statusInput = document.createElement('input');
            statusInput.type = 'hidden';
            statusInput.name = 'status';
            statusInput.value = button.value;
            popoverContent.appendChild(statusInput);
            
            const link = document.createElement('input');
            link.type = 'hidden';
            link.name = 'link';
            link.value = window.location.href;
            popoverContent.appendChild(link);
            popoverContent.submit(); // Submit the form
          });
        });

        return popoverContent;
      }
    });

    popoverTriggerEl.addEventListener('shown.bs.popover', function() {
      const popoverContainer = document.querySelector('.popover');
      document.addEventListener('click', closePopover);

      function closePopover(event) {
        if (!popoverContainer.contains(event.target) || event.target.tagName === 'BUTTON') {
          popover.hide();
          document.removeEventListener('click', closePopover);
        }
      }
    });

    return popover;
  });
});
