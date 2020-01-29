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

## internal complaint review policy
* complaint_review
 - utter_complaint_review

## code of ethical conduct 
* code_of_conduct
 - utter_code_of_conduct

## alchohol/drugs consumption
* drugs
 - utter_drugs

# employee referal
* emp_refer
 - utter_emp_refer

## communication
* communication
 - utter_communication

## confidentiality
* confidentiality
 - utter_confidentiality

## intellect_prop
* intellect_prop
 - utter_intellect_prop

## job performance
* job
 - utter_job

## appraisal
* appraisal
- utter_appraisal

## variable pay
* variable
 - utter_variable

## pip
* pip
 - utter_pip

## race award
* race
 - utter_race

## pf and esi emp benefits
* pf_esi
 - utter_pf_esi

## gratuity
* gratuity
 - utter_gratuity

## mediclaim
* mediclaim
 - utter_mediclaim

## extra work hours
* extra_work
 - utter_extra_work

## meal vouchers
* meals
 - utter_meals

## deputation policy
* deputation
 - utter_deputation

## travel policy
* travel
 - utter_travel

## resignation policy
* resign
 - utter_resign

## seperation
* seperation
 - utter_seperation

## disciplinary
* disciplinary
 - utter_disciplinary

## gardening
* gardening
 - utter_gardening

## exit interview
* exit_interview
 - utter_exit_interview

## protection of environment 
* env_protection
 - utter_env_protection

## rules of conduct
* rule_of_conduct
 - utter_rule_of_conduct

## whistleblower
* whistleblower
 - utter_whistleblower

## contract employee policy
* contract_emp
 - utter_contract_emp
 
