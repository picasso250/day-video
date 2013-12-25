day-video
=========

Record you action per day to an hour video and watch it.

将一段时间的屏幕活动录下来，压缩成视频播放。

Important
-------------

It cost disk space, about 0.5G per hour.

How to use
-------------

First, run record.py to record screen.

```bash
python record.py
```

Press Control-C to stop recording.

Then use export.sh to export to video.

```bash
bash export.sh
```

Dependencies
-------------

- mencoder
