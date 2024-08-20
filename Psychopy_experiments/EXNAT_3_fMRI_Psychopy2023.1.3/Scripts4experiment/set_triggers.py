### Prepare triggers

time_after_trigger = 0.003  # wait for 3ms after a trigger before clearing the line with the 0 trigger

### List of Trigger Values
trigger_map = {
    'block_onset': 2,
    'response_target': 4,
    #'response_continue': 6,
    'trial_onset': 8,
    #'click_training_onset': 10,
    'Reading_pseudotext_no_click_onset': 12,
    'Reading_Baseline_main_no_click_onset': 14,
    #'1back_single_training1_onset': 16,
    #'1back_single_training2_onset': 18,
    '1back_single_main_no_click_onset': 20,
    '1back_dual_main_no_click_onset': 22,
    #'2back_single_training1_onset': 24,
    #'2back_single_training2_onset': 26,
    '2back_single_main_no_click_onset': 28,
    '2back_dual_main_no_click_onset': 30,
    #'prediction_tendency_task_onset': 32,
    #'visual_task_main_onset': 34,
    #'visual_task_training_onset': 36,
    'block_offset': 38,
    #'freq_440_onset': 40,
    #'freq_440_offset': 42,
    #'freq_587_onset': 44,
    #'freq_587_offset': 46,
    #'freq_782_onset': 48,
    #'freq_782_offset': 50,
    #'freq_1043_onset': 52,
    #'freq_1043_offset': 54,
    #'ordered_onset': 56,
    #'random_onset': 58,
    'start_experiment': 60,
    'end_experiment': 62,
    'trial_offset': 64,
    'eyetracking_baseline': 66,
    'test_trigger': 68
}

# Function to send trigger value by specifying event name
def send_trigger(event_name):
    # get corresponding trigger value:
    trigger_value = trigger_map[event_name]

    # send trigger to Eyetracker:
    el_tracker.sendMessage(event_name)

send_trigger(event_name='start_experiment')