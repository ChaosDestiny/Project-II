## happy path1
* greet
  - utter_greet
  - action_check_name
* mood_great
  - utter_ask_happyreason
* mood_great_reason
  - utter_happy

## happy path2
* mood_great_reason
  - utter_happy

## happy path3
* mood_great
  - utter_ask_happyreason
* mood_great_reason
  - utter_happy
  
## unhappy path1
* greet
  - utter_greet
  - action_check_name
* mood_unhappy
  - utter_ask_unhappyreason
* mood_unhappy_reason
  - utter_unhappy
  - utter_ask_action

## unhappy path2
* mood_unhappy
  - utter_ask_unhappyreason
* mood_unhappy_reason
  - utter_unhappy
  - utter_ask_action
  
## unhappy path3
* mood_unhappy_reason
  - utter_unhappy
  - utter_ask_action

## unhappy path4
* mood_unhappy_reason
  - utter_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## unhappy path5
* mood_unhappy_reason
  - utter_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_unhappy
  - utter_ask_action

## unhappy path6
* mood_unhappy
  - utter_ask_unhappyreason
* mood_unhappy_reason
  - utter_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_unhappy
  - utter_ask_action
  
## get name + info 1
* get_name
  - utter_ask_name
* name{"name": "Kẹo"} 
  - slot{"name": "Kẹo"}
  - utter_thanks
  - utter_ask_info
* affirm
  - utter_ask_hobby
* hobby{"hobby": "đọc sách"} 
  - slot{"color": "đọc sách"} 
  - utter_ask_color
* color{"color": "đỏ"} 
  - slot{"color": "đỏ"} 
  - utter_ask_food
* food{"food": "mỳ xào"} 
  - slot{"food": "mỳ xào"} 
  - utter_thanks
  - utter_ask_action

## get name + info 2
* get_name
  - utter_ask_name
* name{"name": "Kẹo"} 
  - slot{"name": "Kẹo"}
  - utter_thanks
  - utter_ask_info
* deny
  - utter_ask_action

## name first
* name{"name": "Hùng"}
  - slot{"name": "Hùng"}
  - utter_ask_action
  
## deny
* deny
  - utter_ask_action
* deny
  - utter_goodbye
  
## sad path 1
* greet
  - utter_greet
  - action_check_name
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 1.1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_unhappy
  
## sad path 2
* greet
  - utter_greet
  - action_check_name
* mood_unhappy
  - utter_cheer_up
  - utter_suggest_song
* deny
  - utter_goodbye
  
## sad path 2
* greet
  - utter_greet
  - action_check_name
* mood_unhappy
  - utter_cheer_up
  - utter_suggest_song
* affirm
    - action_play_music
* play_music{"song": "1 phút"}
    - slot{"song": "1 phút"}
    - action_play_music
    - utter_did_that_help
* affirm
    - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## play music
* greet
    - utter_greet
    - action_check_name
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ismusic_good

## play music + ismusic_good 1
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ismusic_good
* affirm
    - utter_happy

## play music + ismusic_good 2
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ismusic_good
* deny
    - utter_unhappy
    
## play music 2
* greet
    - utter_greet
    - action_check_name
* play_music{"song": "Con cò bé bé"}
    - slot{"song": "Con cò bé bé"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* goodbye
    - utter_goodbye
 
## play music 3
* greet
    - utter_greet
    - action_check_name
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* deny
    - utter_goodbye

## play music 4
* play_music
    - utter_ask_song
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ismusic_good
* affirm
    - utter_happy  

## play music 5
* play_music
    - utter_ask_song
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ismusic_good
* deny
    - utter_unhappy  
    - utter_ask_action
    
## play music 6
* play_music
    - utter_ask_song
* play_music{"song": "Faded"}
    - slot{"song": "Faded"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* tell_story
    - action_tell_story
* tell_story{"story": "Cô bé lọ lem"}
    - slot{"story": "Cô bé lọ lem"}
    - action_tell_story

## play music 7
* greet
    - utter_greet
    - action_check_name
* play_music
    - utter_ask_song

## play music 8
* play_music
    - utter_ask_song
    
## tell story 1
* tell_story
    - utter_ask_story
    
## tell story 2
* greet
    - utter_greet
    - action_check_name
* tell_story
    - utter_ask_story
* tell_story{"story": "Cô bé bán diêm"}
    - slot{"story": "Cô bé bán diêm"}
    - action_tell_story
    - utter_ask_tell_again
* affirm
    - action_tell_story
    - utter_ask_tell_again
* deny
    - utter_ask_action
    
## tell story 3
* greet
    - utter_greet
    - action_check_name
* tell_story{"story": "Thạch Sanh"}
    - slot{"story": "Thạch Sanh"}
    - action_tell_story
    - utter_ask_tell_again
* deny
    - utter_ask_action
    
## tell story 4
* greet
    - utter_greet
    - action_check_name
* tell_story{"story": "Tấm cám"}
    - slot{"story": "Tấm cám"}
    - action_tell_story
    - utter_ask_tell_again
* deny
    - utter_ask_action
* deny
    - utter_goodbye

## tell story 5
* greet
    - utter_greet
    - action_check_name
* tell_story
    - utter_ask_story
* tell_story{"story": "Cây tre trăm đốt"}
    - slot{"story": "Cây tre trăm đốt"}
    - action_tell_story
    - utter_isstory_good
* affirm
    - utter_happy

## tell story 6
* greet
    - utter_greet
    - action_check_name
* tell_story{"story": "Cây khế"}
    - slot{"story": "Cây khế"}
    - action_tell_story
    - utter_isstory_good
* deny
    - utter_unhappy

## read poem 1
* greet
    - utter_greet
    - action_check_name
* read_poem
    - utter_ask_poem
* read_poem{"poem": "Lượm"}
    - slot{"poem": "Lượm"}
    - action_read_poem
    - utter_ispoem_good
* affirm
    - utter_happy

## read poem 2
* greet
    - utter_greet
    - action_check_name
* read_poem
    - utter_ask_poem
* read_poem{"poem": "Ông đồ"}
    - slot{"poem": "Ông đồ"}
    - action_read_poem
    - utter_ispoem_good
* deny
    - utter_unhappy
    - utter_ask_action
    
## read poem 3
* greet
    - utter_greet
    - action_check_name
* read_poem
    - utter_ask_poem
* read_poem{"poem": "Từ ấy"}
    - slot{"poem": "Từ ấy"}
    - action_read_poem
    - utter_ask_read_again
* affirm
    - action_read_poem
    - utter_ispoem_good
* affirm
    - utter_happy
    
## read poem 4
* read_poem{"poem": "nhớ rừng"}
    - slot{"poem": "nhớ rừng"}
    - action_read_poem
    - utter_ispoem_good
* affirm
    - utter_happy
    
## read poem 5
* greet
    - utter_greet
    - action_check_name
* read_poem
    - utter_ask_poem
* read_poem{"poem": "qua đèo ngang"}
    - slot{"poem": "qua đèo ngang"}
    - action_read_poem
    - utter_ask_read_again
* deny
    - utter_ask_action

## read poem 6
* read_poem
    - utter_ask_poem
* read_poem{"poem": "bánh trôi nước"}
    - slot{"poem": "bánh trôi nước"}
    - action_read_poem
    - utter_ask_read_again
* affirm
    - action_read_poem
    - utter_ispoem_good
* deny
    - utter_unhappy
    - utter_ask_action

## read poem 7
* read_poem
    - utter_ask_poem
* read_poem{"poem": "việt bắc"}
    - slot{"poem": "việt bắc"}
    - action_read_poem
    - utter_ispoem_good
* affirm
    - utter_happy
    
## using
* greet
    - utter_greet
    - action_check_name
* using
    - utter_using
    
## stop
* stop
  - utter_stop
 
## using
* greet
  - utter_greet
  - action_check_name
* who
  - utter_me
  
## who_am_i
* who_am_i
  - action_your_name
    
## praise
* praise
  - utter_thanks
    
## disparage
* disparage
  - utter_improve
    
## who
* who
  - utter_me
    
## using
* greet
  - utter_greet
  - action_check_name
* who_am_i
  - action_your_name

## deny
* deny
  - utter_ask_action
* affirm
  - utter_suggest_song