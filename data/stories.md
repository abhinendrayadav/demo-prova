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
 
<!-- * concern
 - utter_click_button
 - action_send_it_email
 - utter_ask_more -->

<!-- ## when it directly start with it
* inform{"ticket":"ithelpdesk"}
 - utter_ask_what -->
<!-- * concern
 - utter_click_button
 - action_send_it_email
 - utter_ask_more -->

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

<!-- * greet
    - utter_greet
* mood_unhappy
    - utter_feedback -->
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

 ## reminder confirm
 - action_reminder
* mood_great
 - action_thinkhr