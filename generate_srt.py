import os
from aeneas.executetask import ExecuteTask
from aeneas.task import Task

def generate_srt(audio_path, text_path, srt_path, lang="cmn"):
    """
    使用 aeneas 对齐音频和文本，输出 .srt 字幕。
    audio_path:   .mp3 音频路径
    text_path:    纯文本歌词路径，每行一句
    srt_path:     输出 .srt 路径
    lang:         语言代码，普通话用 "cmn"
    """
    # 配置对齐参数
    config_string = f"task_language={lang}|is_text_type=plain|os_task_file_format=srt"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = os.path.abspath(audio_path)
    task.text_file_path_absolute = os.path.abspath(text_path)
    task.sync_map_file_path_absolute = os.path.abspath(srt_path)

    # 执行对齐
    ExecuteTask(task).execute()
    task.output_sync_map_file()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="根据 mp3 和歌词生成 .srt 字幕")
    parser.add_argument("audio",  help="输入音频文件 (.mp3)")
    parser.add_argument("text",   help="已另存为纯文本的歌词文件 (.txt，每行一句)")
    parser.add_argument("output", help="输出 .srt 字幕文件路径")
    args = parser.parse_args()

    generate_srt(args.audio, args.text, args.output)
    print(f"已生成字幕：{args.output}")