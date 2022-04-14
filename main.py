from system_lib import *


def main():
    system = System()
    while True:
        if system.reset_button.is_pushed():
            system.reset()

        # Check if tray is empty
        if system.is_mask_tray_empty():
            system.report_empty()
            # And skip all the following processes and directly wait for the reset
            system.HALT()
            # When the HALT is over, go back to the beginning of the loop
            continue

        # Detect masks in stack and display
        system.display_stack_level()

        # Detect whether the mask is being transmitted
        # (this mask should not be transmitting, if it is, an error will be reported
        if system.is_mask_in_transit():
            system.report_fault()
            # And skip all the following processes and directly wait for the reset
            system.HALT()
            # When the HALT is over, go back to the beginning of the loop
            continue
        else:
            system.turn_on_led(LED_READY)
            # The mask machine is started,
            # waiting for the customer to issue a mask request
            system.wait_request()

        # Here, it means that a customer has come to the door
        system.dispensing_mask()
        # TODO You can't simply go directly to the next step here, because the motor dispensing_mask takes time.
        # Maybe add a time.sleep(), but not necessarily useful
        # Discuss this with your group members

        # Check if the mask has been removed from the stack correctly
        if not system.is_mask_in_waiting_position():
            system.report_fault()
            # And skip all the following processes and directly wait for the reset
            system.HALT()
            # When the HALT is over, go back to the beginning of the loop
            continue

        # Hand out the mask and wait until
        system.release_mask_partially_and_wait()

        # Detect if the mask has been taken by the guest, and if not,
        # force the mask to be pushed out completely
        if system.is_mask_still_waiting_collection():
            system.release_mask_totally()
            # TODO Here you can't simply go to the next step, because the motor release_mask_totally takes time.
            # Maybe add a time.sleep(), but not necessarily useful
            # Discuss this with group members

        # Check again whether the masks are all pushed out, if not, report an error
        if system.is_mask_still_waiting_collection():
            system.report_fault()
            # And skip all the following processes and directly wait for the reset
            system.HALT()
            # When the HALT is over, go back to the beginning of the loop
            continue

        # Close the door, and send data to the GUI
        system.close_door()
        system.stack_count -= 1
        system.send_current_stack_count()
        system.reset_report_led()
        # TODO You can't simply go directly to the next loop here, because the motor close_door takes time.
        # Maybe add a time.sleep(), but not necessarily useful
        # Discuss this with group members


if __name__ == "__main__":
    main()
