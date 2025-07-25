STRINGS = {
    'en': {
        "select_language": "Select language (1: Korean, 2: English): ",
        "invalid_input": "Invalid input. Please try again.",
        "select_bot": "# Select prompt file #",
        "bot_option_custom": "Custom prompt input",
        "no_prompts_found": "No prompt files found in prompts directory.",
        "select_prompt_message": "Select (1-{num_options} or C): ",
        "enter_prompt_filename": "Enter prompt filename (under ./prompts): ",
        "mode_selected": "Language: {lang_upper} | Prompt: {prompt_filepath}",
        "error_no_api_key": "[Error] OPENROUTER_API_KEY not found in environment variables.",
        "fetching_models": "Fetching model metadata from OpenRouter...",
        "fetching_models_failed": "Failed to fetch model list",
        "error_file_not_found": "[Error] File not found: {filepath}",
        "error_no_headers": "[Error] No headers found in: {filepath}",
        "error_no_project_name": "[Error] No 'project name' section in prompt file.",
        "error_no_system_prompt": "[Error] No 'system prompt' section.",
        "research_start": "### Research started for: {project_name} ###",
        "output_folder_info": "Outputs will be saved in: {output_dir}",
        "live_log_info": "Live logs will be recorded.",
        "models_in_use": "Models: {models_list}",
        "collaboration_disabled": "[COLLABORATION DISABLED]",
        "prompt_execution": "[Prompt {prompt_id}/{total_prompts}] Executing: {prompt_name}",
        "reasoning_activated": "(Reasoning mode ON)",
        "request_start": "{num_models} models: Running requests...",
        "task_completed": "Response complete for: {nick}",
        "task_failed": "FAILED: No response: {nick}",
        "task_error": "[ERROR] {model_nickname}: {e}",
        "prompt_finished": "-- Prompt {prompt_id} finished. --",
        "all_finished": "# All prompts processed. #",
        "log_reasoning_header": "\n## REASONING MODE LOG ##\n",
        "log_prompt_header": "\n{divider} Prompt {prompt_id}: {prompt_name} {divider}\n",
        "log_error_message": ">>> Error occurred: {e}\n",
        "log_error_header": "\n## ERROR OCCURRED ##\n{error_message}\n",
        "prompts_dir_not_found": "Error: prompts directory not found",
        "no_description": "(no description)",
        "file_column": "File",
        "description_column": "Description",
        "custom_file_path": "Enter custom file path",
    },
    'ko': {
        "select_language": "언어를 선택하세요 (1: 한글, 2: 영어): ",
        "invalid_input": "잘못된 입력입니다. 다시 시도해주세요.",
        "select_bot": "# 프롬프트 파일 선택 #",
        "bot_option_custom": "커스텀 프롬프트 입력",
        "no_prompts_found": "prompts 디렉토리에 프롬프트 파일이 없습니다.",
        "select_prompt_message": "선택 (1-{num_options} 또는 C): ",
        "enter_prompt_filename": "프롬프트 파일명을 입력하세요 (./prompts 하위): ",
        "mode_selected": "언어: {lang_upper} | 프롬프트: {prompt_filepath}",
        "error_no_api_key": "[오류] 환경 변수에서 OPENROUTER_API_KEY를 찾을 수 없습니다.",
        "fetching_models": "OpenRouter로부터 모델 메타데이터를 불러오는 중...",
        "fetching_models_failed": "모델 목록 불러오기 실패",
        "error_file_not_found": "[오류] 파일 없음: {filepath}",
        "error_no_headers": "[오류] 헤더가 없는 프롬프트 파일: {filepath}",
        "error_no_project_name": "[오류] 프롬프트 파일에 'project name' 섹션이 없습니다.",
        "error_no_system_prompt": "[오류] 'system prompt' 섹션이 없습니다.",
        "research_start": "### 프로젝트 리서치 시작: {project_name} ###",
        "output_folder_info": "출력물 폴더: {output_dir}",
        "live_log_info": "실시간 로그가 기록됩니다.",
        "models_in_use": "사용 모델: {models_list}",
        "collaboration_disabled": "[협업 비활성화]",
        "prompt_execution": "[프롬프트 {prompt_id}/{total_prompts}] 실행 중: {prompt_name}",
        "reasoning_activated": "(추론 모드 활성화)",
        "request_start": "{num_models}개 모델: 요청 실행 중...",
        "task_completed": "응답 완료: {nick}",
        "task_failed": "실패: 응답 없음: {nick}",
        "task_error": "[오류] {model_nickname}: {e}",
        "prompt_finished": "-- 프롬프트 {prompt_id} 완료 --",
        "all_finished": "# 모든 프롬프트 처리 완료 #",
        "log_reasoning_header": "\n## 추론 모드 로그 ##\n",
        "log_prompt_header": "\n{divider} 프롬프트 {prompt_id}: {prompt_name} {divider}\n",
        "log_error_message": ">>> 오류 발생: {e}\n",
        "log_error_header": "\n## 오류 발생 ##\n{error_message}\n",
        "prompts_dir_not_found": "오류: prompts 디렉토리를 찾을 수 없습니다",
        "no_description": "(설명 없음)",
        "file_column": "파일",
        "description_column": "설명",
        "custom_file_path": "커스텀 파일 경로 입력",
    }
}