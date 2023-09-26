import os
from slack_bolt import App
import parseresults

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    parseresults.get_test_xml_from_file(open(os.environ.get("TEST_RESULTS_PATH"), 'r'))
    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "callback_id": "home_view",

                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Test results - most recent build",
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": parseresults.present_test_header()
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Details",
                                },
                                "value": "button_details",
                                "action_id": "actionId-0"
                            }
                        ]
                    }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("actionId-0")
def show_latest_details(ack, client, body, logger):
    ack()
    parseresults.get_test_xml_from_file(open(os.environ.get("TEST_RESULTS_PATH"), 'r'))
    try:
        view = {
            "type": "modal",
            "callback_id": "view_1",

            "title": {"type": "plain_text", "text": "My App"},
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Test results - most recent build",
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": parseresults.present_test_header()
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Details",
                    }
                },
            ]
        }
        details = parseresults.present_all_fixtures()
        for d in details:
            view["blocks"].append({"type": "section", "text": {"type": "mrkdwn", "text": d}})
        client.views_open(
            trigger_id=body["trigger_id"],
            view=view
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


if __name__ == '__main__':
    parseresults.get_test_xml_from_file(open(os.environ.get("TEST_RESULTS_PATH"), 'r'))
    app.start(port=int(os.environ.get("PORT", 3000)))
