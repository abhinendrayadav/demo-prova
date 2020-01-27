## lnd_story_response_selector
* lndFAQ
  - respond_lndFAQ
  - utter_ask_more

## lnd acc lock
* lnd_lock
  - utter_acc_lock
  - action_acc_lock
  - utter_ask_more

## lnd status
* lnd_status
  - utter_status
  - action_status
  - utter_ask_more

## lnd_thinkhr
* lnd_thinkhr
  - utter_thinkhr
  - action_thinkhr
  - utter_ask_more

## ext traininghs
* lnd_ext_trainings
  - utter_ext_training
  - action_ext_trainings
  - utter_ask_more

## curse story
* curse
  - utter_curse_response

## mail IT with entity extracted
* raise_ticket{"ticket":"ithelpdesk"}
 - utter_ask_what

## concern
* concern
 - utter_click_button
 - action_send_it_email
 - utter_ask_more

## mail it without entity
* raise_ticket
 - utter_which_ticket
* inform{"ticket":"ithelpdesk"}
 - utter_ask_what
 
## greet with user saying happy and neutral

* greet
    - utter_greet
* mood_great
    - utter_thanks_ask

## greet with user saying sad and giving reason

* greet
    - utter_greet
* mood_unhappy
    - utter_feedback

## mood sad
* affirm
    - utter_sad_reason
    - action_listen
    - utter_thanks_ask

## thanks 
* thanks
    - utter_thanks_reply

## greet with user saying sad and denying for feedback
* deny
    - utter_thanks_ask

## outlook

* outlook_issue
 - utter_click_button
 - action_send_it_email
 - utter_ask_more

## thanks and bye 
* thanks+goodbye
 - utter_thanks_reply
 - utter_goodbye

## mobile phone usage policy
* mobile_usage
 - utter_mobile_usage

## voice mails, files, emails lockers access
* access_mails
 - utter_access_mails
 
## internet usage policy
* internet_usage
 - utter_internet_usage

## software access procedure
* access_sw
 - utter_access_sw

## remote access to email account
* remote_email_policy
 - utter_remote_email_policy

## internet based mail access
* internet_based_emails
 - utter_internet_based_emails

## encryption of emails
* email_encryption
 - utter_email_encryption

## email monitoring
* email_monitoring
 - utter_email_monitoring

## disclaimer
* disclaimer
 - utter_disclaimer

## public holidays
* public_holidays
 - utter_public_holidays

## leave procedure
* leave_procedure
 - utter_leave_procedure


## lwp and lop
* lwp_lop
 - utter_lwp_lop

## mtp 
* mtp
 - utter_mtp

## adoption leave
* adoption_leave
 - utter_adoption_leave

## paternity leave
* paternity_leave
 - utter_paternity_leave

## harrasment policy
* harrasment_policy
 - utter_harrasment_policy