import asyncio
import logging
import aioschedule as schedule


class Sсheduler:
    tasks_config: dict
    
    
    def __init__(self, tasks_config: dict) -> None:
         self.tasks_config = tasks_config

    async def add_tasks(self):
        for task, config in self.tasks_config.items():
            task = config['schedule'](config['task'])
            logging.info(f'Task is running: {task}')

    async def run(self):
        logging.info('Scheduler worker is runnig...')
        await self.add_tasks()
        while True:
            await schedule.run_pending()
            await asyncio.sleep(1) 
     