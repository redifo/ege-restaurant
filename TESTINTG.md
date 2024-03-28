# **Testing**

[Go back to the README](README.md)

## **Table of Contents**

* [**Testing**](#testing)
  * [**Table of Contents**](#table-of-contents)
  * [**Manual Testing**](#manual-testing)
  * [**User Story Testing**](#user-story-testing)
    * [**Role-based restrictions**](#role-based-restrictions)
    * [**CSV Upload**](#csv-upload)
  * [**Accessibility Testing**](#accessibility-testing)
  * [**Lighthouse Testing**](#lighthouse-testing)
  * [**Validation**](#validation)
    * [**HTML Validation**](#html-validation)
    * [**CSS Validation**](#css-validation)
    * [**JavaScript Validation**](#javascript-validation)
    * [**Python Validation**](#python-validation)
  * [**Bugs and Fixes**](#bugs-and-fixes)

## User-Based Restrictions

During testing, I discovered a vulnerability where users could manipulate reservation data by manually typing reservation IDs into the browser URL. This posed a security risk as users could potentially edit reservations that weren't theirs. To address this issue:

Manual Reservation ID Entry: Identified that users could manipulate reservation data by manually typing reservation IDs into the browser URL.
Edit Reservation View (views.py): Implemented a validation check within the edit_reservation view to ensure that only the owner of the reservation could edit it. Added logic to verify the user's ownership before allowing any modifications.
Custom 403 Template: Created a custom 403 template to handle unauthorized access attempts. This template specifically addresses the issue of users attempting to edit reservations that they don't own, providing a clear message and preventing any unauthorized actions.
By implementing these measures, user-based restrictions have been enforced to ensure data integrity and protect user privacy within the reservation system.

## Manual testing

### Admin Testing

| TEST                                             | OUTCOME                                                    | PASS/FAIL |
|--------------------------------------------------|------------------------------------------------------------|-----------|
| Create Menu Item                                 | Menu item successfully created and displayed               | Pass      |
| Edit Menu Item                                   | Menu item details updated successfully                     | Pass      |
| Delete Menu Item                                 | Menu item deleted successfully                             | Pass      |
| Create User                                      | User successfully created and displayed                    | Pass      |
| Edit User                                        | User details updated successfully                          | Pass      |
| Delete User                                      | User deleted successfully                                  | Pass      |
| Create Reservation                               | Reservation successfully created and displayed             | Pass      |
| Edit Reservation                                 | Reservation details updated successfully                    | Pass      |
| Delete Reservation                               | Reservation deleted successfully                           | Pass      |
| Create Table                                     | Table successfully created and displayed                   | Pass      |
| Edit Table                                       | Table details updated successfully                         | Pass      |
| Delete Table                                     | Table deleted successfully                                 | Pass      |

### User Testing

| TEST                                             | OUTCOME                                                    | PASS/FAIL |
|--------------------------------------------------|------------------------------------------------------------|-----------|
| View Menu Items                                  | Menu items displayed correctly                             | Pass      |
| Create Reservation                               | Reservation successfully created and displayed             | Pass      |
| Edit Own Reservation                             | Own reservation details updated successfully                | Pass      |
| Delete Own Reservation                           | Own reservation deleted successfully                        | Pass      |

## **Validation**

### **HTML Validation**
* 

### **CSS Validation**
* 

### **JavaScript Validation**
* 

### **Python Validation**
* 


