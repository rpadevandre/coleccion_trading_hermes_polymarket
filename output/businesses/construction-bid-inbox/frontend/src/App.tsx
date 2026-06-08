import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import BidInboxDemo from './views/BidInboxDemo';
import PipelineCalculator from './views/PipelineCalculator';
import TradeFitForm from './views/TradeFitForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'bid-inbox-demo': BidInboxDemo,
  'pipeline-calculator': PipelineCalculator,
  'trade-fit-form': TradeFitForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('bid-inbox-demo')} className={route === 'bid-inbox-demo' ? 'active' : ''}>BidInboxDemo</button>
          <button onClick={() => setRoute('pipeline-calculator')} className={route === 'pipeline-calculator' ? 'active' : ''}>PipelineCalculator</button>
          <button onClick={() => setRoute('trade-fit-form')} className={route === 'trade-fit-form' ? 'active' : ''}>TradeFitForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
