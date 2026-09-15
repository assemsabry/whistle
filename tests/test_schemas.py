from whistle.core.schemas import Detection, Track


def test_detection_serializes_bbox_as_json_array():
    item = Detection(3, "player", (1.0, 2.0, 10.0, 20.0), 0.9)
    assert item.to_dict() == {
        "frame_id": 3,
        "class_name": "player",
        "bbox_xyxy": [1.0, 2.0, 10.0, 20.0],
        "confidence": 0.9,
    }


def test_track_serializes_stable_fields():
    item = Track(7, 3, "referee", (0.0, 1.0, 2.0, 3.0), 0.8)
    assert item.to_dict()["track_id"] == 7
