
__mod_name__ = "Playback ⏯"

__help__ = """
𝙲𝙾𝙼𝙼𝙰𝙽𝙳
𝙋𝙇𝘼𝙔𝘽𝘼𝘾𝙆
- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist."""

__command_list__ = ["player"], ["skip"], ["pause"], ["resume"], ["end"], ["current"], ["playlist"]
__handlers__ = [player, skip, pause, resume, end, current, playlist]
